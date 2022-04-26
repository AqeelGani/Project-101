import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, folders, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root,file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,
                                    mode = dropbox.files.WriteMode.overwrite)


def main():
    access_token='sl.BGZY3GtP8WxHJIC2-25Ank_7A7v02C9DFiR_D8gnOy3a5fxQcS1KYid8sNknalT2XVptTWOjQgO1z80mLJ_N_reRHxHH4QVHmv4aA_KzALhliV7fS8PjzcBS53sHZUSRRTKU0Yqh'
    transferData=TransferData(access_token)

    file_from=input('Enter The Source : ')
    file_to=input('Enter The Destination : ')

    transferData.upload_file(file_from, file_to)
    print('File Uploaded Successfully!')

if __name__ == '__main__':
    main()
