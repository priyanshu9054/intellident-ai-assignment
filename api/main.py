from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from PIL import Image

app = FastAPI(title="IntelliDent AI - Image Upload API")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_messages = []
    for error in exc.errors():
        # Filter out 'body' from the location to make it cleaner
        field = ".".join(str(x) for x in error["loc"] if x not in ("body",))
        error_messages.append(f"{field}: {error['msg']}")
    
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Failed",
            "errors": error_messages
        }
    )


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    """
    Accepts an image and returns basic metadata.
    """
    image = Image.open(file.file)

    return {
        "success": True,
        "message": "Image processed successfully",
        "data": {
            "filename": file.filename,
            "format": image.format,
            "width": image.width,
            "height": image.height
        }
    }
