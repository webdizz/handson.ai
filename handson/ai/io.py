import urllib.request as req
import os

IO_CHUNK_SIZE = 1024


def get_file_from(url, filename):
    """Encapsulates capability to download big file from given URL in the efficient way.

    Args:
        url: The URL to download file from.
        filename: The name of the file where downloaded content will be saved.

    Returns:
        The absolute path to downloaded file.

    """
    if not os.path.exists(filename):
        request = req.Request(url)
        request.add_header('User-Agent', 'curl/7.55.1')

        print('Is about to download file {} from {}'.format(filename, url))

        response = req.urlopen(request)
        with open(filename, 'wb') as file:
            while True:
                chunk = response.read(IO_CHUNK_SIZE)
                if not chunk:
                    break
                file.write(chunk)
    else:
        print('File {} already exist, will not download again'.format(filename))

    return "{}/{}".format(os.getcwd(), filename)