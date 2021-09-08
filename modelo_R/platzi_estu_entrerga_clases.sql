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
-- Table structure for table `clases`
--

DROP TABLE IF EXISTS `clases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clases` (
  `idclases` int NOT NULL,
  `idcursos_academicos` int NOT NULL,
  `idescuela` int NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `clases_envivo` tinyint(1) DEFAULT NULL,
  `fecha_clase_vivo` datetime DEFAULT NULL,
  `enlace` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`idclases`),
  KEY `fk_idcursos_academicos_idx` (`idcursos_academicos`),
  KEY `fk_idescuelas_idx` (`idescuela`),
  CONSTRAINT `fk_id_escuelas` FOREIGN KEY (`idescuela`) REFERENCES `escuelas` (`idescuelas`),
  CONSTRAINT `fk_idcursos_academicos` FOREIGN KEY (`idcursos_academicos`) REFERENCES `cursos_academicos` (`idcursos_academicos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clases`
--

LOCK TABLES `clases` WRITE;
/*!40000 ALTER TABLE `clases` DISABLE KEYS */;
INSERT INTO `clases` VALUES (1,1,1,'python_1',1,'2021-10-01 00:00:00','asd12390d90g89df/231sdf_Sdfs'),(2,1,1,'python_2',1,'2021-10-04 00:00:00','1s52d5f465as2'),(3,1,1,'python_3',1,'2021-10-08 00:00:00','2d3as5d1qw32s'),(4,1,1,'python_4',1,'2021-11-08 00:00:00','235asd52asdas'),(5,1,1,'python_5',1,'2021-11-04 00:00:00','125d2a5dqw5e2re'),(6,1,1,'python_6',1,'2021-12-05 00:00:00','2d4as8f5a2sdaf'),(7,1,1,'python_7',1,'2021-12-08 00:00:00','2asdiolkfsd'),(8,1,1,'python_8',1,'2021-12-09 00:00:00','231asdiosklklasd'),(9,1,1,'python_9',NULL,NULL,NULL),(10,1,1,'python_10',NULL,NULL,NULL),(11,2,1,'angular_1',NULL,NULL,NULL),(12,2,1,'angular_2',NULL,NULL,NULL),(13,2,1,'angular_3',1,'2021-11-01 00:00:00','asd12390d90g89df/231sdf_Sdfs'),(14,2,1,'angular_4',1,'2021-12-01 00:00:00','asd12390d90g89df/231sdf_Sdfs'),(15,2,1,'angular_5',1,'2021-12-08 00:00:00','12525645321jnoiuudt'),(16,2,1,'angular_6',1,'2021-12-15 00:00:00','sdjasiooplñsadijaklsd'),(17,2,1,'angular_7',1,'2021-12-16 00:00:00','asdioflkopqw4lk234'),(18,2,1,'angular_8',1,'2021-12-28 00:00:00','89980asdklkl23489sdflk'),(19,3,2,'pintura_1',1,'2021-09-01 00:00:00','asdasdpwoaasd'),(20,3,2,'pintura_2',1,'2021-09-15 00:00:00','2s45d89fa52s5d'),(21,3,2,'pintura_3',NULL,NULL,NULL),(22,3,2,'pintura_4',NULL,NULL,NULL),(23,3,2,'pintura_5',NULL,NULL,NULL),(24,3,2,'pintura_6',1,'2021-09-18 00:00:00','2012s5d8f5as5'),(25,3,2,'pintura_7',NULL,NULL,NULL),(26,3,2,'pintura_8',NULL,NULL,NULL),(27,3,2,'pintura_9',NULL,NULL,NULL),(28,4,2,'oleo_1',1,'2021-11-01 00:00:00','3215sd2qwefa'),(29,4,2,'oleo_2',1,'2021-11-03 00:00:00','2sad56qwe2asf564asd'),(30,4,2,'oleo_3',1,'2021-11-05 00:00:00','231as56d7qwffad'),(31,4,2,'oleo_4',NULL,NULL,NULL),(32,4,2,'oleo_5',NULL,NULL,NULL),(33,4,2,'oleo_6',NULL,NULL,NULL),(34,4,2,'oleo_7',1,'2021-11-20 00:00:00','asd25dsf897q52we'),(35,4,2,'oleo_8',1,'2021-11-24 00:00:00','231asd56fsd23w'),(36,5,3,'contaduria_1',1,'2021-09-15 00:00:00','2sad564qweasd'),(37,5,3,'contaduria_2',1,'2021-09-20 00:00:00','23asd564qwe'),(38,5,3,'contaduria_3',1,'2021-09-25 00:00:00','23as05das32'),(39,5,3,'contaduria_4',1,'2021-09-28 00:00:00','2sd564d89qw564asf'),(40,5,3,'contaduria_5',1,'2021-09-30 00:00:00','2sd564qw23as8gfdf'),(41,5,3,'contaduria_6',1,'2021-10-30 00:00:00','23ad56qwefdsas'),(42,5,3,'contaduria_7',NULL,NULL,NULL),(43,6,3,'finanzas_1',1,'2021-11-20 00:00:00','32sd56qw23e'),(44,6,3,'finanzas_2',1,'2021-11-22 00:00:00','32asd23qw54e'),(45,6,3,'finanazas_3',NULL,NULL,NULL),(46,6,3,'finanzas_4',NULL,NULL,NULL);
/*!40000 ALTER TABLE `clases` ENABLE KEYS */;
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
