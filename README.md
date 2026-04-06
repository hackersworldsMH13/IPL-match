# IPL Match Project Documentation

## Features
- Feature 1: Real-time score updates
- Feature 2: Player statistics
- Feature 3: Match schedule and results

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hackersworldsMH13/IPL-match.git
   ```
2. Navigate to the project directory:
   ```bash
   cd IPL-match
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

## Usage
- To run the application:
   ```bash
   npm start
   ```
- Open your browser and go to `http://localhost:3000`

## Troubleshooting
- If you experience issues, check the following:
  - Ensure all dependencies are installed correctly.
  - Check your network connection if you're fetching data from an external API.

## API Response Format
- The API returns data in JSON format:
  ```json
  {
    "status": "success",
    "data": {
      "match": {
        "id": "123",
        "home_team": "Team A",
        "away_team": "Team B",
        "score": "0 - 0",
        "status": "In Progress"
      }
    }
  }
  ```

For additional information, refer to the API documentation and user manuals.