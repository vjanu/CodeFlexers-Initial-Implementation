-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2019 at 05:32 PM
-- Server version: 5.7.11
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `plus_go`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `UserID` varchar(20) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Name` varchar(200) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`UserID`, `Username`, `Password`, `Name`) VALUES
('U1557930336556', '1', '1', '1'),
('U1557930741930', '11', '11', '111'),
('U1557930912772', '2', '2', '2');

-- --------------------------------------------------------

--
-- Table structure for table `payment_details`
--

CREATE TABLE `payment_details` (
  `PaymentID` varchar(20) NOT NULL,
  `UserID` varchar(20) NOT NULL,
  `CardNo` bigint(16) NOT NULL,
  `ExDate` varchar(5) NOT NULL,
  `CVC` int(3) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment_details`
--

INSERT INTO `payment_details` (`PaymentID`, `UserID`, `CardNo`, `ExDate`, `CVC`) VALUES
('PAY1558281697542', 'U1558278875790', 4512453423567893, '03/22', 543),
('PAY1558285007339', 'U15582788567670', 4512453423567893, '03/22', 543);

-- --------------------------------------------------------

--
-- Table structure for table `preference`
--

CREATE TABLE `preference` (
  `PID` varchar(20) NOT NULL,
  `UserID` varchar(20) NOT NULL,
  `GenderP` varchar(20) NOT NULL,
  `LanguageS` varchar(20) NOT NULL,
  `Smoking` varchar(20) NOT NULL,
  `MusicLover` varchar(20) NOT NULL,
  `MotionSickness` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `preference`
--

INSERT INTO `preference` (`PID`, `UserID`, `GenderP`, `LanguageS`, `Smoking`, `MusicLover`, `MotionSickness`) VALUES
('PRF1558287056775', '456789f', 'yes', 'sinhala', 'no', 'no', 'yes'),
('PRF1558287059519', 'f', 'yes', 'sinhala', 'no', 'no', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `rating_copassenger`
--

CREATE TABLE `rating_copassenger` (
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

CREATE TABLE `rating_driver` (
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

CREATE TABLE `rating_vehicle` (
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
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UserID` varchar(20) NOT NULL,
  `FullName` varchar(250) NOT NULL,
  `Profession` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `DOB` varchar(50) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `RName` varchar(255) NOT NULL,
  `RPhone` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UserID`, `FullName`, `Profession`, `Email`, `DOB`, `Gender`, `RName`, `RPhone`) VALUES
('U1558278875734', '4 4', 'Ectu', '4@g.c', '1111/09/09', 'Male', 'Rosh top', 344545453),
('U1558278454734', '4 4', 'Ectu', '4@g.c', '1111/09/09', 'Male', 'Rosh top', 344545453),
('U1590278454734', '4 4', 'Ectu', '4@g.c', '1111/09/09', 'Male', 'Rosh top', 344545453);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `VehicleID` varchar(255) NOT NULL,
  `UserID` varchar(255) NOT NULL,
  `Brand` varchar(50) NOT NULL,
  `Model` varchar(50) NOT NULL,
  `VNumber` varchar(50) NOT NULL,
  `Mileage` varchar(50) NOT NULL,
  `MYear` varchar(50) NOT NULL,
  `RYear` varchar(50) NOT NULL,
  `FuelType` varchar(50) NOT NULL,
  `TType` varchar(50) NOT NULL,
  `EngineCapacity` varchar(50) NOT NULL,
  `FrontView` varchar(100) NOT NULL,
  `BackView` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`VehicleID`, `UserID`, `Brand`, `Model`, `VNumber`, `Mileage`, `MYear`, `RYear`, `FuelType`, `TType`, `EngineCapacity`, `FrontView`, `BackView`) VALUES
('V1558286100676', 'U123456787', 'sdfghj', 'hj', '2345g', '100', '1990', 'i7', 'jk', 'sddfghj', '33456gfhhj', '456789', 'fgthjk');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `payment_details`
--
ALTER TABLE `payment_details`
  ADD PRIMARY KEY (`PaymentID`),
  ADD UNIQUE KEY `UserID` (`UserID`);

--
-- Indexes for table `preference`
--
ALTER TABLE `preference`
  ADD PRIMARY KEY (`PID`),
  ADD UNIQUE KEY `UserID` (`UserID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`VehicleID`),
  ADD UNIQUE KEY `UserID` (`UserID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
