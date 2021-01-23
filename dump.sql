CREATE DATABASE  IF NOT EXISTS `ebooksportal` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ebooksportal`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: ebooksportal
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_book`
--

DROP TABLE IF EXISTS `ep_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `attachment` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `create_date` date NOT NULL,
  `downloads` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_book_tags`
--

DROP TABLE IF EXISTS `ep_book_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_book_tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ep_book_tags_book_id_tag_id_0d1561ed_uniq` (`book_id`,`tag_id`),
  KEY `ep_book_tags_tag_id_602dcc1c_fk_ep_tag_id` (`tag_id`),
  CONSTRAINT `ep_book_tags_book_id_0d4dc663_fk_ep_book_id` FOREIGN KEY (`book_id`) REFERENCES `ep_book` (`id`),
  CONSTRAINT `ep_book_tags_tag_id_602dcc1c_fk_ep_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `ep_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=196 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_paper`
--

DROP TABLE IF EXISTS `ep_paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_paper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `attachment` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `create_date` date NOT NULL,
  `downloads` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_paper_tags`
--

DROP TABLE IF EXISTS `ep_paper_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_paper_tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `paper_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ep_paper_tags_paper_id_tag_id_fc94c7de_uniq` (`paper_id`,`tag_id`),
  KEY `ep_paper_tags_tag_id_5cb17f18_fk_ep_tag_id` (`tag_id`),
  CONSTRAINT `ep_paper_tags_paper_id_effc0096_fk_ep_paper_id` FOREIGN KEY (`paper_id`) REFERENCES `ep_paper` (`id`),
  CONSTRAINT `ep_paper_tags_tag_id_5cb17f18_fk_ep_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `ep_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_section`
--

DROP TABLE IF EXISTS `ep_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_section` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `category` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_section_books`
--

DROP TABLE IF EXISTS `ep_section_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_section_books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `section_id` int NOT NULL,
  `book_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ep_section_books_section_id_book_id_000fab97_uniq` (`section_id`,`book_id`),
  KEY `ep_section_books_book_id_f552600f_fk_ep_book_id` (`book_id`),
  CONSTRAINT `ep_section_books_book_id_f552600f_fk_ep_book_id` FOREIGN KEY (`book_id`) REFERENCES `ep_book` (`id`),
  CONSTRAINT `ep_section_books_section_id_7e785c22_fk_ep_section_id` FOREIGN KEY (`section_id`) REFERENCES `ep_section` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_section_papers`
--

DROP TABLE IF EXISTS `ep_section_papers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_section_papers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `section_id` int NOT NULL,
  `paper_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ep_section_papers_section_id_paper_id_b4073861_uniq` (`section_id`,`paper_id`),
  KEY `ep_section_papers_paper_id_17d66f5e_fk_ep_paper_id` (`paper_id`),
  CONSTRAINT `ep_section_papers_paper_id_17d66f5e_fk_ep_paper_id` FOREIGN KEY (`paper_id`) REFERENCES `ep_paper` (`id`),
  CONSTRAINT `ep_section_papers_section_id_eb8d1e99_fk_ep_section_id` FOREIGN KEY (`section_id`) REFERENCES `ep_section` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ep_tag`
--

DROP TABLE IF EXISTS `ep_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ep_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'ebooksportal'
--

--
-- Dumping routines for database 'ebooksportal'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-23  9:05:59
