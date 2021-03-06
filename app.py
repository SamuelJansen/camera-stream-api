import globals
from python_framework import initialize
globalsInstance = globals.newGlobalsInstance(
    __file__
    , settingStatus = True
    , successStatus = True
    , errorStatus = True
    , debugStatus = True
    , failureStatus = True

    # , warningStatus = True
    # , wrapperStatus = True
    # , logStatus = True
    # , testStatus = True
    # , printRootPathStatus = False
)

import CameraStream
app = CameraStream.app
api = CameraStream.api
jwt = CameraStream.jwt

@initialize(api, defaultUrl = '/swagger', openInBrowser=False)
def runFlaskApplication(app):
    app.run(debug=False, use_reloader=False)

if __name__ == '__main__' :
    runFlaskApplication(app)
