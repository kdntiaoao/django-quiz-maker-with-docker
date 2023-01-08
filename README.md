# django-quiz-maker-with-docker

- Django プロジェクトを作成する

  ```
  $ docker-compose run web django-admin startproject config .
  ```

- Docker イメージのビルド

  ```
  $ docker-compose build
  ```

- Docker コンテナの起動

  ```
  $ docker-compose up -d

  # ビルドも実行する
  $ docker-compose up -d --build
  ```

- Docker コンテナの停止

  ```
  $ docker-compose down

  # コンテナ、イメージ、ボリュームも削除する
  $ docker-compose down --rmi all --volumes --remove-orphans
  ```

- superuser の作成

  ```
  $ docker-compose run web python3 manage.py createsuperuser
  ```

- アプリの作成

  ```
  $ docker-compose run web python3 manage.py startapp myapp
  ```
