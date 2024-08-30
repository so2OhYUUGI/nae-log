# NaeLOG Setup Guide

NaeLOGは、Raspberry Piとの統合を通じて育苗の支援を行うウェブベースのアプリケーションです。ユーザーは育成用照明の設定を管理し、温度や湿度を記録し、これらのパラメーターをウェブインターフェースを介して表示できます。

## 1. Frontend Setup

### Prerequisites

- Node.js and yarn are required.

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/so2OhYUUGI/nae-log.git
   cd nae-log
   ```

2. Install dependencies:

   ```
   yarn install
   ```

### Development Server

To start the development server:

```
yarn start
```

### Frontend Build

To build the frontend for production:

```
yarn run build
```

The build files will be output to the `public` directory, which can be served by any static file server.

## 2. Backend Setup

### Prerequisites

- Python 3.x
- Raspberry Pi with the necessary hardware setup.

### Virtual Environment Setup

1. Create a virtual environment:

   ```
   python -m venv .venv --upgrade-deps --system-site-packages
   ```

2. Activate the virtual environment:

   - **Windows:**
     ```
     .\.venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```
     source .venv/bin/activate
     ```

3. Install required libraries:

   ```
   pip install "fastapi[standard]" uvicorn apscheduler 'strawberry-graphql[fastapi]' sqlalchemy
   ```

4. Deactivate the virtual environment after use:

   ```
   deactivate
   ```

## 3. Running the Backend

1. Use the following command to start the FastAPI server:

   ```
   cd backend
   uvicorn app.main:app --reload --host=0.0.0.0 --port=80
   ```

This setup guide provides a complete overview for setting up both the frontend and backend environments for NaeLOG.
