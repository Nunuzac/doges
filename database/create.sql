create schema doges;

create table doges.role (
	id serial not null,
	name varchar not null unique,
	primary key (id)
);

create table doges.user (
	id int not null,
	name varchar not null,
	hash varchar not null,
	email varchar not null unique,
	role_id int not null,
	primary key (id),
	foreign key (role_id) references doges.role(id)
);

create table doges.breed (
	id serial not null,
	name varchar not null unique,
	primary key (id)
);

create table doges.dog (
	id serial not null,
	name varchar not null,
	breed_id int not null,
	color varchar not null,
	primary key (id),
	foreign key (breed_id) references doges.breed(id)
);

create table doges.parenthood (
	user_id int not null,
	dog_id int not null,
	date date not null,
	primary key (user_id, dog_id),
	foreign key (user_id) references doges.user(id),
	foreign key (dog_id) references doges.dog(id)
);

create user django with password '123Django';

grant usage on schema doges to django;
grant select, insert, update on all tables in schema doges to django;
grant select, update on all sequences in schema doges to django;