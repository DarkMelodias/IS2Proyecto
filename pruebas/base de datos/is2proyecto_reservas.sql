-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: is2proyecto
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservas` (
  `id_reserva` int NOT NULL AUTO_INCREMENT,
  `materiales` varchar(90) NOT NULL,
  `equipos` varchar(90) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `Laboratorio_num_laboratorio` int NOT NULL,
  `Materiales_cod_material` int NOT NULL,
  `Equipos_cod_equipo` int NOT NULL,
  `usuarios_user` varchar(45) NOT NULL,
  PRIMARY KEY (`id_reserva`,`Laboratorio_num_laboratorio`,`Materiales_cod_material`,`Equipos_cod_equipo`,`usuarios_user`),
  KEY `fk_Reservas_Laboratorio1_idx` (`Laboratorio_num_laboratorio`),
  KEY `fk_Reservas_Materiales1_idx` (`Materiales_cod_material`),
  KEY `fk_Reservas_Equipos1_idx` (`Equipos_cod_equipo`),
  KEY `fk_Reservas_usuarios1_idx` (`usuarios_user`),
  CONSTRAINT `fk_Reservas_Equipos1` FOREIGN KEY (`Equipos_cod_equipo`) REFERENCES `equipos` (`cod_equipo`),
  CONSTRAINT `fk_Reservas_Laboratorio1` FOREIGN KEY (`Laboratorio_num_laboratorio`) REFERENCES `laboratorio` (`num_laboratorio`),
  CONSTRAINT `fk_Reservas_Materiales1` FOREIGN KEY (`Materiales_cod_material`) REFERENCES `materiales` (`cod_material`),
  CONSTRAINT `fk_Reservas_usuarios1` FOREIGN KEY (`usuarios_user`) REFERENCES `usuarios` (`user`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
INSERT INTO `reservas` VALUES (12,'Oro,','ninguno,','2022-10-11','10:00:00',2,2,0,'admin');
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-15 21:02:01
