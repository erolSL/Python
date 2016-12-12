-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 29 Eki 2016, 11:59:37
-- Sunucu sürümü: 5.6.17
-- PHP Sürümü: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Veritabanı: `debe`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `changed`
--

CREATE TABLE IF NOT EXISTS `changed` (
  `changedID` int(11) NOT NULL AUTO_INCREMENT,
  `isim` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `deger` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `userID` int(11) NOT NULL,
  PRIMARY KEY (`changedID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `odalar`
--

CREATE TABLE IF NOT EXISTS `odalar` (
  `odalarID` int(11) NOT NULL AUTO_INCREMENT,
  `isim` varchar(255) DEFAULT NULL,
  `deger` varchar(255) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  PRIMARY KEY (`odalarID`),
  KEY `fk_ODALAR_1` (`userID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=16 ;

--
-- Tablo döküm verisi `odalar`
--

INSERT INTO `odalar` (`odalarID`, `isim`, `deger`, `userID`) VALUES
(1, 'oda1', 'erol', 1),
(2, 'oda6', '6', 1),
(3, 'oda2', '2', 1),
(4, 'oda3', '3', 1),
(5, 'oda4', '4', 1),
(6, 'oda5', '5', 1),
(7, 'oda7', '7', 2),
(8, 'oda8', '8', 2),
(9, 'oda9', '9', 2),
(10, 'oda10', '10', 2),
(11, 'oda11', '11', 2),
(12, 'oda12', '12', 2),
(15, 'oda8', '8', 1);

--
-- Tetikleyiciler `odalar`
--
DROP TRIGGER IF EXISTS `TakipOda`;
DELIMITER //
CREATE TRIGGER `TakipOda` AFTER UPDATE ON `odalar`
 FOR EACH ROW BEGIN

	INSERT INTO changed
		( isim, deger, userID )
	VALUES
		( new.isim, new.deger, new.userID );

END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_turkish_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=3 ;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`username`, `email`, `password`, `create_time`, `userID`) VALUES
('erol.uslu', 'erol.uslu@bil.omu.edu.tr', '1234567890', '2017-06-18 04:08:14', 1),
('kirac', 'kirac@hotmail.com', '1234567890', '2016-10-18 06:09:13', 2);

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `odalar`
--
ALTER TABLE `odalar`
  ADD CONSTRAINT `fk_ODALAR_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
