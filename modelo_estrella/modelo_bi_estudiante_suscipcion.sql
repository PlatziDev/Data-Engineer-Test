-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: modelo_bi
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

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
-- Table structure for table `estudiante_suscipcion`
--

DROP TABLE IF EXISTS `estudiante_suscipcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante_suscipcion` (
  `idestudiante_suscipciones` int NOT NULL AUTO_INCREMENT,
  `idestudiante_suscipcion` int NOT NULL,
  `anio` varchar(4) NOT NULL,
  `mes` varchar(2) NOT NULL,
  `dia` varchar(2) NOT NULL,
  PRIMARY KEY (`idestudiante_suscipciones`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante_suscipcion`
--

LOCK TABLES `estudiante_suscipcion` WRITE;
/*!40000 ALTER TABLE `estudiante_suscipcion` DISABLE KEYS */;
INSERT INTO `estudiante_suscipcion` VALUES (1,1,'2021','10','01'),(2,2,'2021','09','02'),(3,3,'2021','08','01'),(4,4,'2021','08','04'),(5,5,'2021','08','09'),(6,6,'2021','07','10'),(7,7,'2021','07','12'),(8,8,'2021','07','29'),(9,9,'2021','08','30'),(10,10,'2021','09','01'),(11,11,'2021','08','01'),(12,12,'2021','08','01'),(13,13,'2021','08','01');
/*!40000 ALTER TABLE `estudiante_suscipcion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-07 19:29:16
