# WebAuthnRepeater.py - Burp Extension to decode/edit WebAuthn requests

from burp import IBurpExtender, IMessageEditorTabFactory, IMessageEditorTab
from java.io import PrintWriter
import base64
import json

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._stdout = PrintWriter(callbacks.getStdout(), True)

        callbacks.setExtensionName("WebAuthn Repeater")
        callbacks.registerMessageEditorTabFactory(self)
        self._stdout.println("[+] WebAuthn Repeater loaded.")

    def createNewInstance(self, controller, editable):
        return WebAuthnTab(self, controller, editable)

class WebAuthnTab(IMessageEditorTab):
    def __init__(self, extender, controller, editable):
        self._extender = extender
        self._helpers = extender._helpers
        self._editable = editable
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(editable)

    def getTabCaption(self):
        return "WebAuthn"

    def getUiComponent(self):
        return self._txtInput.getComponent()

    def isEnabled(self, content, isRequest):
        try:
            body = self._helpers.bytesToString(content)
            if 'clientDataJSON' in body or 'attestationObject' in body:
                return True
        except:
            pass
        return False

    def setMessage(self, content, isRequest):
        if content is None:
            self._txtInput.setText("")
            self._txtInput.setEditable(False)
            return

        body = self._helpers.bytesToString(content)
        try:
            data = json.loads(body)
            decoded = {}
            for key in ["clientDataJSON", "attestationObject", "authenticatorData"]:
                if key in data:
                    try:
                        decoded[key] = json.loads(base64.urlsafe_b64decode(data[key] + "=="))
                    except Exception:
                        decoded[key] = "[Could not decode as JSON]"

            beautified = json.dumps(decoded, indent=4)
            self._txtInput.setText(beautified)
        except:
            self._txtInput.setText("[Error parsing request body]")

    def getMessage(self):
        return None  # Keeps the original request unless manually modified

    def isModified(self):
        return False

    def getSelectedData(self):
        return self._txtInput.getSelectedText()
