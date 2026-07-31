

# docstring
def url_logger(base_env: dict[str, int] | str | None , url: str | None  , *args: int,  **kwargs: str) -> None:
    """
    This function will log all url params to TEMP/endpoint_usage.txt

    :param base_env: base_env, can be dev, stage, prod
    :param url: url, can be example.com or tes-example.com
    :param args: users who will call this endpoint
    :param kwargs: query parameters for get endpoints
    :return: None
    """

    # if not isinstance(url, str):
    #     raise TypeError('url must be a string')

    print(f'Sending request to {base_env}-{url}')
    print(f'with parameters: {kwargs}')
    print(f'this request is available for {args}')



url_logger('dev', 'http://....com', 'us1', 'us2', sort_by='asd')

