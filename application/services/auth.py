from utils.config import config
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN


api_key_header = APIKeyHeader(name="X-API-KEY-Token", auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    print(config.API_KEY)
    if api_key_header == config.API_KEY:
        return api_key_header   
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Ivalid API KEY"
        )
