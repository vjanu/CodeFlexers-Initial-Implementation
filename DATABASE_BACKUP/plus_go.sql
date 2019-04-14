-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 03, 2019 at 04:39 AM
-- Server version: 5.5.24-log
-- PHP Version: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `plus_go`
--

-- --------------------------------------------------------

--
-- Table structure for table `rating_copassenger`
--

CREATE TABLE IF NOT EXISTS `rating_copassenger` (
  `tripId` varchar(50) NOT NULL,
  `CopassengerId` varchar(255) NOT NULL,
  `RatedBy` varchar(255) NOT NULL,
  `GivenRating` varchar(20) NOT NULL,
  `CalcualtedRating` varchar(20) NOT NULL,
  `AverageRating` varchar(20) NOT NULL,
  `Dissatisfaction` varchar(255) DEFAULT NULL,
  `Sentiment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rating_driver`
--

CREATE TABLE IF NOT EXISTS `rating_driver` (
  `TripId` varchar(50) NOT NULL,
  `DriverId` varchar(255) NOT NULL,
  `RatedBy` varchar(255) NOT NULL,
  `GivenRating` varchar(20) NOT NULL,
  `CalculatedRating` varchar(20) NOT NULL,
  `AverageRating` varchar(20) NOT NULL,
  `Compliment` varchar(255) DEFAULT NULL,
  `Dissatisfaction` varchar(255) DEFAULT NULL,
  `Sentiment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rating_vehicle`
--

CREATE TABLE IF NOT EXISTS `rating_vehicle` (
  `tripId` varchar(50) NOT NULL,
  `vehicleId` varchar(255) NOT NULL,
  `RatedBy` varchar(255) NOT NULL,
  `GivenRating` varchar(20) NOT NULL,
  `CalculatedRating` varchar(20) NOT NULL,
  `AverageRating` varchar(20) NOT NULL,
  `Dissatisfaction` varchar(255) DEFAULT NULL,
  `Sentiment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `UId` varchar(255) NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `NIC` varchar(20) NOT NULL,
  `OverallRating` varchar(20) NOT NULL DEFAULT '5'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE IF NOT EXISTS `vehicle` (
  `VehicleId` varchar(255) NOT NULL,
  `UId` varchar(255) NOT NULL,
  `Model` varchar(20) NOT NULL,
  `vehicleRating` varchar(20) NOT NULL DEFAULT '5'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
