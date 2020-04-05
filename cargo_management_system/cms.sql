-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: cargoms_db
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.18.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add admin profile',7,'add_adminprofile'),(26,'Can change admin profile',7,'change_adminprofile'),(27,'Can delete admin profile',7,'delete_adminprofile'),(28,'Can view admin profile',7,'view_adminprofile'),(29,'Can add bill details',8,'add_billdetails'),(30,'Can change bill details',8,'change_billdetails'),(31,'Can delete bill details',8,'delete_billdetails'),(32,'Can view bill details',8,'view_billdetails'),(33,'Can add consign details',9,'add_consigndetails'),(34,'Can change consign details',9,'change_consigndetails'),(35,'Can delete consign details',9,'delete_consigndetails'),(36,'Can view consign details',9,'view_consigndetails'),(37,'Can add transc details',10,'add_transcdetails'),(38,'Can change transc details',10,'change_transcdetails'),(39,'Can delete transc details',10,'delete_transcdetails'),(40,'Can view transc details',10,'view_transcdetails'),(41,'Can add employee_ details',11,'add_employee_details'),(42,'Can change employee_ details',11,'change_employee_details'),(43,'Can delete employee_ details',11,'delete_employee_details'),(44,'Can view employee_ details',11,'view_employee_details'),(45,'Can add per_table',12,'add_per_table'),(46,'Can change per_table',12,'change_per_table'),(47,'Can delete per_table',12,'delete_per_table'),(48,'Can view per_table',12,'view_per_table');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$vzd0rcB3HjUi$vJaBRre1FrcY//VFRUI0uViMtFYN5rmJ1AqJMc9+k5s=',NULL,0,'gps123','','','guru@gmail.com',0,1,'2020-03-20 16:10:18.404569'),(2,'pbkdf2_sha256$180000$y4i3PKIRUK5C$vDyU8Fgq4vzbLBZTvETKjkj+B8LLSv5l688C9KpIxoo=',NULL,0,'gps124','','','guru1@gmail.com',0,1,'2020-03-20 16:12:43.303361'),(3,'pbkdf2_sha256$180000$XfDGPBvVlqHb$pUgAxbpyGAm1urWuJ0cvMjyBIkSCvxbwMVEEUHw/7C4=','2020-03-21 11:34:52.708709',0,'gps125','','','guru2@gmail.com',0,1,'2020-03-20 16:13:51.408044'),(4,'pbkdf2_sha256$180000$jqPgjgDaBVqF$JOhnwYgaq1rZI1tiRN+FWBZrYa4gQundYK86aT5Q+9g=','2020-03-31 07:31:55.029321',0,'gps126','','','guru3@gmail.com',0,1,'2020-03-20 16:15:10.589128'),(5,'pbkdf2_sha256$180000$bIURgehbj9kX$xYh0k8qh1zSfYO1WKmwcRvLbEdokw1tLix1CXrpeLzg=','2020-03-27 15:05:03.750875',0,'guru123','','','gps.g@gmail.com',0,1,'2020-03-25 19:03:05.812341'),(6,'pbkdf2_sha256$180000$ZEIRvllV961O$GNtVQbX4YJMw6cSiP+153PhaXbpcki0s3HZhHZfBfPk=','2020-03-25 19:51:39.788661',0,'gps121','','','gurt1@gmail.com',0,1,'2020-03-25 19:51:07.563860'),(7,'pbkdf2_sha256$180000$z0HJk0dI7Puq$77bahnMhrf20h3Q1vP1ecMZ5TahSLq4shSahmE8Jn08=','2020-04-01 08:32:57.163842',0,'kar222','','','rahul@gmail.com',0,1,'2020-03-31 07:40:07.312559');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_billdetails`
--

DROP TABLE IF EXISTS `cargoms_billdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_billdetails` (
  `b_id` int(11) NOT NULL,
  `b_desc` longtext NOT NULL,
  `b_amt` int(11) NOT NULL,
  `b_ship` longtext NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_billdetails`
--

LOCK TABLES `cargoms_billdetails` WRITE;
/*!40000 ALTER TABLE `cargoms_billdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargoms_billdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_consigndetails`
--

DROP TABLE IF EXISTS `cargoms_consigndetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_consigndetails` (
  `c_id` int(11) NOT NULL,
  `c_desc` longtext NOT NULL,
  `c_quan` int(11) NOT NULL,
  `c_price` int(11) NOT NULL,
  `c_to` longtext NOT NULL,
  `c_from` longtext NOT NULL,
  `c_date` date NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_consigndetails`
--

LOCK TABLES `cargoms_consigndetails` WRITE;
/*!40000 ALTER TABLE `cargoms_consigndetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargoms_consigndetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_cust_details`
--

DROP TABLE IF EXISTS `cargoms_cust_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_cust_details` (
  `order_id` int(11) NOT NULL,
  `cust_name` varchar(45) NOT NULL,
  `s_contact` varchar(10) NOT NULL,
  `s_add` varchar(100) NOT NULL,
  `s_city` varchar(30) NOT NULL,
  `s_pincode` int(11) NOT NULL,
  `r_name` varchar(45) NOT NULL,
  `r_contact` varchar(10) NOT NULL,
  `r_add` varchar(100) NOT NULL,
  `r_city` varchar(30) NOT NULL,
  `r_pincode` int(11) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_cust_details`
--

LOCK TABLES `cargoms_cust_details` WRITE;
/*!40000 ALTER TABLE `cargoms_cust_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargoms_cust_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_cust_pkg_details`
--

DROP TABLE IF EXISTS `cargoms_cust_pkg_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_cust_pkg_details` (
  `order_id` int(11) NOT NULL,
  `cust_name` varchar(45) NOT NULL,
  `pkg_r_date` date NOT NULL,
  `pkg_r_time` time(6) NOT NULL,
  `pkg_d_date` date NOT NULL,
  `pkg_d_time` time(6) NOT NULL,
  `pkg_weight` int(11) NOT NULL,
  `pkg_ship_add` longtext NOT NULL,
  `pkg_ship_city` varchar(45) NOT NULL,
  `pkg_ship_pincode` int(11) NOT NULL,
  `ship_service_type` varchar(45) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_cust_pkg_details`
--

LOCK TABLES `cargoms_cust_pkg_details` WRITE;
/*!40000 ALTER TABLE `cargoms_cust_pkg_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargoms_cust_pkg_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_employee_details`
--

DROP TABLE IF EXISTS `cargoms_employee_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_employee_details` (
  `eid_no` int(11) NOT NULL,
  `e_name` varchar(45) NOT NULL,
  `e_contact` varchar(10) NOT NULL,
  `e_add` longtext NOT NULL,
  `e_mail` varchar(254) NOT NULL,
  `e_userName` varchar(45) NOT NULL,
  `e_per_id` varchar(6) NOT NULL,
  PRIMARY KEY (`eid_no`),
  UNIQUE KEY `e_userName` (`e_userName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_employee_details`
--

LOCK TABLES `cargoms_employee_details` WRITE;
/*!40000 ALTER TABLE `cargoms_employee_details` DISABLE KEYS */;
INSERT INTO `cargoms_employee_details` VALUES (1111,'guru','9809098763','abc','guru3@gmail.com','gps126','000111'),(1211,'rahul singh','9887978786','hhuyedh','rahul@gmail.com','kar222','112122'),(12312,'guru','8787897989','huihu','gurt1@gmail.com','gps121','121122');
/*!40000 ALTER TABLE `cargoms_employee_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_per_table`
--

DROP TABLE IF EXISTS `cargoms_per_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_per_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `per` int(11) NOT NULL,
  `Description` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_per_table`
--

LOCK TABLES `cargoms_per_table` WRITE;
/*!40000 ALTER TABLE `cargoms_per_table` DISABLE KEYS */;
INSERT INTO `cargoms_per_table` VALUES (7,1,'Customer Details'),(8,2,'Cargo Details'),(9,3,'Transaction Details'),(10,4,'Time of Delivery Manegement'),(11,5,'Billing management'),(12,6,'Enquiry');
/*!40000 ALTER TABLE `cargoms_per_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargoms_transc_details`
--

DROP TABLE IF EXISTS `cargoms_transc_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargoms_transc_details` (
  `order_id` int(11) NOT NULL,
  `tr_id` int(11) NOT NULL,
  `t_mode` varchar(20) NOT NULL,
  `t_amt` int(11) NOT NULL,
  `t_date` date NOT NULL,
  `t_time` time(6) NOT NULL,
  `t_status` varchar(20) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargoms_transc_details`
--

LOCK TABLES `cargoms_transc_details` WRITE;
/*!40000 ALTER TABLE `cargoms_transc_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargoms_transc_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'cargoms','adminprofile'),(8,'cargoms','billdetails'),(9,'cargoms','consigndetails'),(11,'cargoms','employee_details'),(12,'cargoms','per_table'),(10,'cargoms','transcdetails'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-03-20 15:06:27.873383'),(2,'auth','0001_initial','2020-03-20 15:06:29.700487'),(3,'admin','0001_initial','2020-03-20 15:06:35.294011'),(4,'admin','0002_logentry_remove_auto_add','2020-03-20 15:06:36.620890'),(5,'admin','0003_logentry_add_action_flag_choices','2020-03-20 15:06:36.678014'),(6,'admin','0004_auto_20200102_1847','2020-03-20 15:06:36.734446'),(7,'admin','0005_auto_20200214_1258','2020-03-20 15:06:36.789118'),(8,'contenttypes','0002_remove_content_type_name','2020-03-20 15:06:37.813773'),(9,'auth','0002_alter_permission_name_max_length','2020-03-20 15:06:37.926212'),(10,'auth','0003_alter_user_email_max_length','2020-03-20 15:06:38.093768'),(11,'auth','0004_alter_user_username_opts','2020-03-20 15:06:38.154595'),(12,'auth','0005_alter_user_last_login_null','2020-03-20 15:06:38.563641'),(13,'auth','0006_require_contenttypes_0002','2020-03-20 15:06:38.596322'),(14,'auth','0007_alter_validators_add_error_messages','2020-03-20 15:06:38.657371'),(15,'auth','0008_alter_user_username_max_length','2020-03-20 15:06:38.793256'),(16,'auth','0009_alter_user_last_name_max_length','2020-03-20 15:06:38.943768'),(17,'auth','0010_alter_group_name_max_length','2020-03-20 15:06:39.089746'),(18,'auth','0011_update_proxy_permissions','2020-03-20 15:06:39.149223'),(19,'auth','0012_auto_20200102_1847','2020-03-20 15:06:39.827732'),(20,'auth','0013_auto_20200214_1258','2020-03-20 15:06:39.952249'),(21,'cargoms','0001_initial','2020-03-20 15:06:40.449753'),(22,'cargoms','0002_auto_20200228_1913','2020-03-20 15:06:40.494921'),(23,'cargoms','0003_auto_20200305_1711','2020-03-20 15:06:45.783291'),(24,'cargoms','0004_auto_20200306_0852','2020-03-20 15:06:55.114784'),(25,'cargoms','0005_auto_20200319_1618','2020-03-20 15:06:57.292133'),(26,'cargoms','0006_auto_20200320_1548','2020-03-20 15:49:07.941338'),(27,'sessions','0001_initial','2020-03-20 15:49:08.358732'),(28,'cargoms','0007_auto_20200320_1602','2020-03-20 16:02:12.920903'),(29,'cargoms','0008_auto_20200320_1606','2020-03-20 16:07:05.124073'),(30,'cargoms','0009_per_table','2020-03-27 10:10:32.537561'),(31,'cargoms','0010_auto_20200327_1019','2020-03-27 10:19:29.087174');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('fcdpbrao08dz50qnpazyzy7kiiwqph5i','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-04 05:54:09.543999'),('kc98qg8mmk6utanirt0eecn1rns1y59e','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-05 14:56:00.499033'),('kxwo4eil5wbnbokh6ii6vilrjrr5dfkr','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-04 05:39:17.315307'),('lto876k9ohiz6vmblj3u1jqhekasaz8c','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-04 05:52:21.392345'),('p4kevjpwrfixf9mem8lo1v1naxorw5q6','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-04 05:09:06.381125'),('pyroenpk61pt2q1zxk1pdvscshvu4kng','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-04 05:27:59.788123'),('t2u3xfq1v27yntnclesmay4lo3z1zxwz','ZWZmZjllOTM0NzM3ZTBiZTZhMjE0OTIxNWI5NjEyMWI5NWEyMDVjZTp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmMmU3ZGE1NjQ2NjI2MmNmNzRjNjAxMjU3YTU5MDY2MzQ4MjE5YWY3In0=','2020-04-15 08:32:57.279468'),('vl6s2kj43pa0ncgcixyc36r8l7fejcou','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-04 05:53:40.880769'),('wmc89kjazv672jhs0qc0bbzhhm3ty86b','ZDVkOTIzYjY0NTA4YzEyZWI5ZDQwNjU1MDI0M2U2ZDE4MTg4ZjM5Njp7fQ==','2020-04-05 14:52:59.577768');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-03 14:21:42
