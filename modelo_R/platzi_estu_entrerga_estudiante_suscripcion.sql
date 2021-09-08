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
-- Table structure for table `estudiante_suscripcion`
--

DROP TABLE IF EXISTS `estudiante_suscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante_suscripcion` (
  `idestudiante_suscripcion` int NOT NULL,
  `idestudiantes` int NOT NULL,
  `idsuscripcion` int NOT NULL,
  `fecha_suscripcion` datetime NOT NULL,
  `idmetodos_de_pago` int NOT NULL,
  `idcortesia` int DEFAULT NULL,
  PRIMARY KEY (`idestudiante_suscripcion`),
  KEY `fk_idmetodopago_idx` (`idmetodos_de_pago`),
  KEY `fk_id_suscripcion_idx` (`idsuscripcion`),
  KEY `fk_estud_cortesia_idx` (`idcortesia`),
  CONSTRAINT `fk_estud_cortesia` FOREIGN KEY (`idcortesia`) REFERENCES `cortesia` (`idcortesia`),
  CONSTRAINT `fk_id_suscripcion` FOREIGN KEY (`idsuscripcion`) REFERENCES `suscripcion` (`idsuscripcion`),
  CONSTRAINT `fk_idmetodopago` FOREIGN KEY (`idmetodos_de_pago`) REFERENCES `metodos_de_pago` (`idmetodos_de_pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante_suscripcion`
--

LOCK TABLES `estudiante_suscripcion` WRITE;
/*!40000 ALTER TABLE `estudiante_suscripcion` DISABLE KEYS */;
INSERT INTO `estudiante_suscripcion` VALUES (1,1,1,'2021-10-01 00:00:00',2,1),(2,2,2,'2021-09-02 00:00:00',3,1),(3,3,1,'2021-08-01 00:00:00',1,1),(4,4,1,'2021-08-04 00:00:00',1,NULL),(5,5,3,'2021-08-09 00:00:00',2,2),(6,6,1,'2021-07-10 00:00:00',2,1),(7,7,1,'2021-07-12 00:00:00',2,1),(8,8,2,'2021-07-29 00:00:00',1,1),(9,9,1,'2021-08-30 00:00:00',2,1),(10,10,2,'2021-09-01 00:00:00',2,1),(11,11,3,'2021-08-01 00:00:00',2,NULL),(12,12,1,'2021-08-01 00:00:00',2,NULL),(13,13,2,'2021-08-01 00:00:00',2,NULL);
/*!40000 ALTER TABLE `estudiante_suscripcion` ENABLE KEYS */;
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
