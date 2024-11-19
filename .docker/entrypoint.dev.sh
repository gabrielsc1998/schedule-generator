#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi

npm install
npm run dev

python manage.py migrate

while sleep 1000; do :; done
