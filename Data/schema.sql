DROP TABLE IF EXISTS guild;
DROP TABLE IF EXISTS role_category;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS stream_channel;
DROP TABLE IF EXISTS twitch_games_followed;

CREATE TABLE guild (
  guild_id INTEGER PRIMARY KEY,
  roles_enabled BOOLEAN DEFAULT FALSE,
  lounges_enabled BOOLEAN DEFAULT FALSE,
  twitch_enabled BOOLEAN DEFAULT FALSE
);

CREATE TABLE role_group (
  rg_id INTEGER PRIMARY KEY AUTOINCREMENT,
  guild_id INTEGER NOT NULL,
  FOREIGN KEY (guild_id) REFERENCES guild (guild_id)
);

CREATE TABLE role (
  symbol TEXT NOT NULL,
  role INTEGER NOT NULL,
  rg_id INTEGER NOT NULL,
  FOREIGN KEY (rg_id) REFERENCES role_group (rg_id)
);

CREATE TABLE stream_channel (
  name TEXT,
  guild_id INTEGER UNIQUE,
  FOREIGN KEY (guild_id) REFERENCES guild (guild_id),
  PRIMARY KEY (name, guild_id)
);

CREATE TABLE twitch_games_followed (
  name TEXT,
  guild_id INTEGER,
  FOREIGN KEY (guild_id) REFERENCES guild (guild_id),
  PRIMARY KEY (name, guild_id)
);