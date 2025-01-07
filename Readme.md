# Telegram Bot: Khodam Game

This repository contains a Telegram bot built using Python and MongoDB, leveraging the `pyrogram` library. The bot introduces a game mechanic where users can engage in battles, upgrade their characters (Khodams), and compete on a leaderboard. The bot is designed to be deployed on any virtual machine (VM) or VPS.

## Features

1. **Set Database for Each Account**:
   - Each user starts with a default Khodam and 50 points.
   - Users can upgrade their Khodam when not engaged in a battle.

2. **Open/Close War**:
   - Open a war to challenge other players. If the user wins, they gain points; if they lose, they lose points.
   - Closing a war removes the user from the active war list.
   - If no action is taken, the status remains empty.

   **Battle Information**:
   - Khodam name (with mention).
   - Attributes: Strength, Health, and Armor.

   **Upgrade**:
   - Upgrades can only be performed when wars are closed.

3. **Khodam Ranking**:
   - A leaderboard displays the rankings of all Khodams based on their points.

4. **Rock-Paper-Scissors Mechanic**:
   - The outcome of battles is determined using the classic Rock-Paper-Scissors game.

## Prerequisites

- Python 3.8+
- MongoDB instance (local or cloud)
- Virtual Machine (VM) or VPS for deployment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/khodam-bot.git
   cd khodam-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the root directory with the following:
     ```env
     API_ID=your_api_id
     API_HASH=your_api_hash
     BOT_TOKEN=your_bot_token
     MONGO_URI=your_mongo_uri
     ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Deployment

The bot can be deployed on any VM or VPS. Ensure the Python environment and MongoDB connection are properly configured. You can use tools like `systemd` or `pm2` to keep the bot running continuously.

## Program Flow

### 1. Set Database for Each Account
- Initialize the database for each user when they start using the bot.
- Users start with a default Khodam and 50 points.

### 2. Open/Close War
- **Open War**: Adds the user to the active war list.
- **Close War**: Removes the user from the active war list.
- **Battle Mechanic**:
  - Players compete in Rock-Paper-Scissors matches.
  - Winners gain points; losers lose points.

### 3. Upgrade
- Users can upgrade their Khodam's attributes (Strength, Health, Armor) only when they are not in a war.

### 4. Ranking
- A leaderboard ranks all Khodams based on their total points.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or bug reports.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
