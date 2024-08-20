# NaeLOG Setup Guide

NaeLOGは、Raspberry Piとの統合を通じて育苗の支援を行うウェブベースのアプリケーションです。ユーザーは育成用照明の設定を管理し、温度や湿度を記録し、これらのパラメーターをウェブインターフェースを介して表示できます。

## 1. Frontend Setup

### Prerequisites

- Node.js and npm are required.

### Installation

1. Clone the repository:

   ```
   git clone <your-repo-url>
   cd NaeLOG
   ```

2. Install dependencies:

   ```
   npm install
   npm install gatsby-plugin-material-ui@next @emotion/react
   npm install @mui/material @emotion/react @emotion/styled --force
   ```

3. Start the development server:

   ```
   gatsby develop
   ```

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
   pip install "fastapi[standard]" uvicorn python-crontab
   ```

4. Deactivate the virtual environment after use:

   ```
   deactivate
   ```

## 3. Running the Backend

1. Use the following command to start the FastAPI server:

   ```
   uvicorn app.main:app --reload --host=0.0.0.0
   ```

This setup guide should provide a solid foundation for setting up both the frontend and backend environments for NaeLOG.
