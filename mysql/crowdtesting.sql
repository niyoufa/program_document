BEGIN;
CREATE TABLE `crowdtesting_customer` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `email` varchar(75) NOT NULL,
    `username` varchar(255) NOT NULL UNIQUE,
    `password` varchar(32) NOT NULL,
    `image_sha1` varchar(40) NOT NULL,
    `time` datetime NOT NULL,
    `last_login` datetime NOT NULL,
    `is_active` bool NOT NULL,
    `phone` varchar(11) NOT NULL,
    UNIQUE (`sha1`),
    UNIQUE (`email`),
    UNIQUE (`username`)
)
;
CREATE TABLE `crowdtesting_tester` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `email` varchar(75) NOT NULL,
    `username` varchar(255) NOT NULL UNIQUE,
    `password` varchar(32) NOT NULL,
    `time` datetime NOT NULL,
    `last_login` datetime NOT NULL,
    `is_active` bool NOT NULL,
    `nick_name` varchar(255) NOT NULL,
    `image_sha1` varchar(40) NOT NULL,
    `age` integer UNSIGNED NOT NULL,
    `gender` smallint NOT NULL,
    `country` integer NOT NULL,
    `education` integer NOT NULL,
    `income` integer NOT NULL,
    `test_experience` integer NOT NULL,
    `used_network_product` integer NOT NULL,
    UNIQUE (`sha1`),
    UNIQUE (`email`),
    UNIQUE (`username`)
)
;
CREATE TABLE `crowdtesting_compaign` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `name` varchar(255) NOT NULL,
    `create_time` datetime NOT NULL,
    `description` longtext NOT NULL,
    `per_cost` double precision NOT NULL,
    `participants_num` integer NOT NULL,
    `arrive_rate` double precision NOT NULL,
    `product_type` integer NOT NULL,
    `url` varchar(200) NOT NULL,
    `url_description` longtext NOT NULL,
    `is_use_template` bool NOT NULL,
    `start_time` datetime NOT NULL,
    `end_time` datetime NOT NULL,
    `status` integer NOT NULL,
    `tester_group_sha1` varchar(40) NOT NULL,
    `test_task_sha1` varchar(40) NOT NULL,
    `customer_sha1_id` integer NOT NULL,
    UNIQUE (`sha1`),
    UNIQUE (`name`, `create_time`)
)
;
ALTER TABLE `crowdtesting_compaign` ADD CONSTRAINT `customer_sha1_id_refs_id_9d351ac4` FOREIGN KEY (`customer_sha1_id`) REFERENCES `crowdtesting_customer` (`id`);
CREATE TABLE `crowdtesting_testergroup` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `name` varchar(255) NOT NULL UNIQUE,
    `description` longtext NOT NULL,
    `age` integer UNSIGNED NOT NULL,
    `gender` smallint NOT NULL,
    `country` integer NOT NULL,
    `education` integer NOT NULL,
    `income` integer NOT NULL,
    `test_experience` integer NOT NULL,
    `used_network_product` integer NOT NULL,
    `compaign_sha1_id` integer NOT NULL UNIQUE,
    UNIQUE (`sha1`),
    UNIQUE (`age`, `gender`, `country`, `education`, `income`, `test_experience`, `used_network_product`)
)
;
ALTER TABLE `crowdtesting_testergroup` ADD CONSTRAINT `compaign_sha1_id_refs_id_c0b6e9ea` FOREIGN KEY (`compaign_sha1_id`) REFERENCES `crowdtesting_compaign` (`id`);
CREATE TABLE `crowdtesting_testergroupmemership` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `group_sha1` varchar(40) NOT NULL,
    `tester_sha1` varchar(40) NOT NULL,
    UNIQUE (`group_sha1`, `tester_sha1`)
)
;
CREATE TABLE `crowdtesting_testtasktemplate` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `task_list` longtext NOT NULL,
    `compaign_sha1_id` integer NOT NULL UNIQUE,
    UNIQUE (`sha1`)
)
;
ALTER TABLE `crowdtesting_testtasktemplate` ADD CONSTRAINT `compaign_sha1_id_refs_id_7a03a908` FOREIGN KEY (`compaign_sha1_id`) REFERENCES `crowdtesting_compaign` (`id`);
CREATE TABLE `crowdtesting_testtasktemplatememership` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `task_sha1` varchar(40) NOT NULL,
    `tester_sha1` varchar(40) NOT NULL,
    `start_time` datetime NOT NULL,
    `end_time` datetime NOT NULL,
    `IP_Address` char(15) NOT NULL,
    `imei_type` integer NOT NULL,
    `status` integer NOT NULL,
    `score` integer NOT NULL,
    UNIQUE (`task_sha1`, `tester_sha1`)
)
;
CREATE TABLE `crowdtesting_radiotask` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `task_content` longtext NOT NULL,
    `task_result` integer NOT NULL,
    UNIQUE (`sha1`)
)
;
CREATE TABLE `crowdtesting_multichoicetask` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `task_content` longtext NOT NULL,
    `task_result` longtext NOT NULL,
    UNIQUE (`sha1`)
)
;
CREATE TABLE `crowdtesting_imageuploadtask` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `task_content` longtext NOT NULL,
    `task_result` varchar(40) NOT NULL,
    UNIQUE (`sha1`)
)
;
CREATE TABLE `crowdtesting_questingansweringtask` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `task_content` longtext NOT NULL,
    `task_result` longtext NOT NULL,
    UNIQUE (`sha1`)
)
;
CREATE TABLE `crowdtesting_fileimage` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sha1` varchar(40) NOT NULL,
    `image` longtext NOT NULL,
    `image_name` varchar(255) NOT NULL,
    `image_size` integer NOT NULL,
    `author` varchar(40) NOT NULL,
    `time` datetime NOT NULL,
    UNIQUE (`sha1`)
)
;
CREATE INDEX `crowdtesting_compaign_4a038c77` ON `crowdtesting_compaign` (`customer_sha1_id`);

COMMIT;
