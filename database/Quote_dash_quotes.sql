-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: localhost    Database: Quote_dash
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(45) NOT NULL,
  `content` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `creator` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_quotes_users_idx` (`creator`),
  CONSTRAINT `fk_quotes_users` FOREIGN KEY (`creator`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotes`
--

LOCK TABLES `quotes` WRITE;
/*!40000 ALTER TABLE `quotes` DISABLE KEYS */;
INSERT INTO `quotes` VALUES (1,' Dr. Seuss','Don\'t cry because it\'s over, smile because it happened.','2019-04-19 09:52:04','2019-04-19 09:52:04',1),(2,'Marilyn Monroe','I\'m selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can\'t handle me at my worst, then you sure as hell don\'t deserve me at my best.','2019-04-19 09:52:51','2019-04-19 09:52:51',4),(3,'Oscar Wilde','Be yourself; everyone else is already taken.','2019-04-19 10:05:19','2019-04-19 10:05:19',1),(4,'Albert Einstein','Two things are infinite: the universe and human stupidity; and I\'m not sure about the universe.','2019-04-19 10:10:51','2019-04-19 10:10:51',3),(5,'Frank Zappa','So many books, so little time.','2019-04-19 11:19:44','2019-04-19 11:19:44',1),(6,'Bernard M. Baruch','Be who you are and say what you feel, because those who mind don\'t matter, and those who matter don\'t mind.','2019-04-19 11:24:10','2019-04-19 11:24:10',2),(7,'Marcus Tullius Cicero','A room without books is like a body without a soul.','2019-04-19 11:33:16','2019-04-19 11:33:16',2),(8,'William W. Purkey','You\'ve gotta dance like there\'s nobody watching, Love like you\'ll never be hurt, Sing like there\'s nobody listening, And live like it\'s heaven on earth.','2019-04-19 11:45:00','2019-04-19 11:45:00',4),(9,'Dr. Seuss','You know you\'re in love when you can\'t fall asleep because reality is finally better than your dreams.','2019-04-19 12:19:53','2019-04-19 12:19:53',5),(12,'Robert Frost','In three words I can sum up everything I\'ve learned about life: it goes on.','2019-04-19 13:10:48','2019-04-19 13:10:48',1),(13,'Eleanor Roosevelt','No one can make you feel inferior without your consent.','2019-04-19 13:11:02','2019-04-19 13:11:02',1),(14,'Mark Twain','If you tell the truth, you don\'t have to remember anything.','2019-04-19 13:14:46','2019-04-19 13:14:46',4);
/*!40000 ALTER TABLE `quotes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-19 13:23:59
