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
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiantes` (
  `idestudiantes` int NOT NULL,
  `documento` bigint NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `idsuscripcion` int NOT NULL,
  `currency` varchar(10) NOT NULL,
  `recurrente` int NOT NULL,
  PRIMARY KEY (`idestudiantes`),
  KEY `fk_idsuscripcion_idx` (`idsuscripcion`),
  CONSTRAINT `fk_idsuscripcion` FOREIGN KEY (`idsuscripcion`) REFERENCES `suscripcion` (`idsuscripcion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiantes`
--

LOCK TABLES `estudiantes` WRITE;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
INSERT INTO `estudiantes` VALUES (1,102452504,'sindy','benitez','3057601523','sindy_benitez@xxxx',1,'peso_cop',1),(2,105048240,'mariana','diez','30540586102','mariana@xxxx',1,'peso_cop',0),(3,103258665,'mateo','torres','312578945','mateo@xxxxx',1,'peso_cop',1),(4,52468215,'jose','marquez','315428652','jose@xxxx',2,'peso_cop',0),(5,35248525,'silvana','pacheco','31652546','silvana@xxxx',2,'peso_cop',1),(6,1012064231,'jacobo','diaz','312545652','jacobo@xxx',2,'peso_cop',0),(7,10231505,'juan manuel','mendez','315489750','jmanuel@xxxx',3,'peso_cop',1),(8,10324525,'carolina','torres','30124525','carolina@xxxx',3,'peso_cop',0),(9,1245625,'angely','gomez','3012054','angely@',3,'peso_cop',1),(10,10258420,'angela','chaparro','3012504','angela@xxx',1,'peso_cop',1),(11,10215245,'valery','santos','32154205','valery@xxx',1,'peso_cop',1),(12,102552425,'teresa','pinzon','320125245','teresa@xxx',1,'peso_cop',0),(13,1021352546,'cristhian','lopez','302452455','cris@xxxx',3,'peso_cop',0);
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;
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
