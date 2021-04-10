DROP TABLE IF EXISTS guild;
DROP TABLE IF EXISTS role_category;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS stream_channel;
DROP TABLE IF EXISTS twitch_games_followed;

CREATE TABLE guild (
  guild_id INTEGER PRIMARY KEY,
  module_roles_enabled BOOLEAN DEFAULT 0,
  module_lounges_enabled BOOLEAN DEFAULT 0,
  module_twitch_enabled BOOLEAN DEFAULT 0
);

CREATE TABLE role_category (
  name TEXT NOT NULL,
  rc_id INTEGER PRIMARY KEY AUTOINCREMENT,
  guild_id INTEGER NOT NULL,
  FOREIGN KEY (guild_id) REFERENCES guild (guild_id)
);

CREATE TABLE role (
  emoji TEXT NOT NULL,
  description TEXT NOT NULL,
  role INTEGER NOT NULL,
  rc_id INTEGER NOT NULL,
  FOREIGN KEY (rc_id) REFERENCES role_category (rc_id)
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