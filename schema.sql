DROP TABLE IF EXISTS server;
DROP TABLE IF EXISTS role_category;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS twitch_games_followed;

CREATE TABLE server (
  id INTEGER PRIMARY KEY,
  roles_enabled BOOLEAN NOT NULL,
  lounges_enabled BOOLEAN NOT NULL,
  twitch_enabled BOOLEAN NOT NULL,
);

CREATE TABLE role_category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  server_id INTEGER NOT NULL,
  FOREIGN KEY (server_id) REFERENCES server (id)
);

CREATE TABLE role (
  symbol TEXT NOT NULL,
  role INTEGER NOT NULL,
  category INTEGER NOT NULL,
  FOREIGN KEY (category) REFERENCES role_category (server_id)
);

CREATE TABLE twitch_games_followed (
  name TEXT,
  server_id INTEGER,
  FOREIGN KEY (server_id) REFERENCES server (id)
);