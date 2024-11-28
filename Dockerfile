FROM python
 
WORKDIR /code

# 左側のローカルのファイルを、右側がコンテナ内のパスにコピーしている
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app
 
CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]