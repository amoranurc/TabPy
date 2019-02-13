from tabpy_server.handlers import ManagementHandler
import os


_QUERY_OBJECT_STAGING_FOLDER = 'staging'


class UploadDestinationHandler(ManagementHandler):
    def initialize(self, tabpy_state, python_service):
        super(UploadDestinationHandler, self).initialize(tabpy_state, python_service)

    def get(self):
        path = self.settings['state_file_path']
        path = os.path.join(path, _QUERY_OBJECT_STAGING_FOLDER)
        self.write({"path": path})
