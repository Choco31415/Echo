DROP TABLE IF EXISTS guild;
DROP TABLE IF EXISTS role_category;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS stream_channel;
DROP TABLE IF EXISTS twitch_games_followed;

CREATE TABLE guild (
  guild_id INTEGER PRIMARY KEY,
  module_react_roles_enabled BOOLEAN DEFAULT 0,
  module_lounges_enabled BOOLEAN DEFAULT 0,
  module_twitch_enabled BOOLEAN DEFAULT 0
);

CREATE TABLE react_role_group (
  react_role_group_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  guild_id INTEGER NOT NULL,
  FOREIGN KEY (guild_id) REFERENCES guild (guild_id)
);

CREATE TABLE react_role (
  react_role_id INTEGER NOT NULL,
  emoji TEXT NOT NULL,
  role TEXT NOT NULL,
  react_role_group_id INTEGER NOT NULL,
  FOREIGN KEY (react_role_group_id) REFERENCES react_role_group (react_role_group_id)
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