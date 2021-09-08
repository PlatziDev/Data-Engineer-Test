-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: platzi_estu_entrerga
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
-- Table structure for table `estados_estudiantes`
--

DROP TABLE IF EXISTS `estados_estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados_estudiantes` (
  `idestados` int NOT NULL,
  `idestados_estudiantes` int NOT NULL,
  `idestudiantes` int NOT NULL,
  PRIMARY KEY (`idestados`),
  KEY `fk_idestados_estudiantes_idx` (`idestados_estudiantes`),
  KEY `fk_idestudiantes_1_idx` (`idestudiantes`),
  CONSTRAINT `fk_idestados_estudiantes` FOREIGN KEY (`idestados_estudiantes`) REFERENCES `estado` (`idestados_estudiantes`),
  CONSTRAINT `fk_idestudiantes_1` FOREIGN KEY (`idestudiantes`) REFERENCES `estudiantes` (`idestudiantes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados_estudiantes`
--

LOCK TABLES `estados_estudiantes` WRITE;
/*!40000 ALTER TABLE `estados_estudiantes` DISABLE KEYS */;
INSERT INTO `estados_estudiantes` VALUES (1,1,1),(2,2,1),(3,1,1),(4,3,1),(5,1,2),(6,2,3),(7,2,4),(8,2,5),(9,2,6),(10,2,7),(11,3,8),(12,2,8),(13,2,9),(14,2,10),(15,2,11),(16,2,12),(17,2,13),(18,1,9),(19,1,10),(20,1,11),(21,1,12);
/*!40000 ALTER TABLE `estados_estudiantes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-07 19:26:47
