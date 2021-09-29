from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import logging
from fastapi.middleware.cors import CORSMiddleware
from remote_controller import RemoteController
from air_monitor import AirMonitor


# utils
def build_filepath(relative_path):
    return os.path.join(os.path.dirname(__file__), relative_path)

# initial setup
app = FastAPI()
logger = logging.getLogger('uvicorn')
remote_controller = RemoteController(17, logger)

try:
    air_monitor = AirMonitor()
except RuntimeError:
    logger.warn('BME680 not found.')

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# define the request body.
class Request(BaseModel):
    target: str
    command: str

# endpoints
@app.post('/control')
async def control(request: Request):
    try:
        remote_controller.transmit(request.target, request.command)
        return {'status': 'ok'}
    except Exception as e:
        logger.error(e)
        return {'status': 'failed'}

@app.get('/test')
async def test():
    return {'status': 'ok'}

@app.get('/air')
async def air():
    try:
        return air_monitor.get()
    except Exception as e:
        logger.error(e)
        return {'detail': 'failed'}

# on_event
@app.on_event('shutdown')
async def shutdown_event():
    remote_controller.cleanup()
    logger.info('Finished RemoteController cleaning up.')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, lifespan='on')
