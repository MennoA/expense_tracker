DROP TABLE IF EXISTS expense;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS currency;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS account;

CREATE TABLE expense (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  amount INTEGER NOT NULL,
  income BOOLEAN NOT NULL,
  tag INTEGER,
  category INTEGER NOT NULL,
  subcat INTEGER,
  image BLOB,
  description TEXT,
  account INTEGER NOT NULL,
  cur INTEGER,
  FOREIGN KEY (tag) REFERENCES tag (id),
  FOREIGN KEY (category) REFERENCES categories (id),
  FOREIGN KEY (subcat) REFERENCES categories (id),
  FOREIGN KEY (account) REFERENCES account (id),
  FOREIGN KEY (cur) REFERENCES currency (id)
);

CREATE TABLE categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  subcat BOOLEAN NOT NULL,
  parent INTEGER,
  description TEXT,
  image BLOB, 
  user INTEGER NOT NULL,
  FOREIGN KEY (parent) REFERENCES categories (id),
  FOREIGN KEY (user) REFERENCES user(id)
);

CREATE TABLE tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL ,
    color TEXT NOT NULL,
    user INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (user) REFERENCES user(id)
);

CREATE TABLE currency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency TEXT NOT NULL,
    fullname TEXT NOT NULL
);

CREATE TABLE account (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    holder INTEGER NOT NULL,
    name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY (holder) REFERENCES user(id)
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL
);

/* populate table */


INSERT INTO currency (currency, fullname) VALUES ('EUR', 'euro');
INSERT INTO currency (currency, fullname) VALUES ('CHF', 'swiss franc');
INSERT INTO currency (currency, fullname) VALUES ('USD', 'united state dollar');
INSERT INTO currency (currency, fullname) VALUES ('JPY', 'japanese yen');