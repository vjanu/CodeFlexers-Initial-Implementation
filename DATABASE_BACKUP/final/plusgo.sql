-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 18, 2019 at 09:22 PM
-- Server version: 8.0.16
-- PHP Version: 7.2.19-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `plusgo`
--

-- --------------------------------------------------------

--
-- Table structure for table `current_passengers`
--

CREATE TABLE `current_passengers` (
  `id` int(11) NOT NULL,
  `tripId` varchar(45) DEFAULT NULL,
  `driverId` varchar(45) DEFAULT NULL,
  `source` varchar(45) DEFAULT NULL,
  `destination` varchar(45) DEFAULT NULL,
  `trip_status` varchar(45) DEFAULT NULL,
  `price` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
('U1560858715472', 'surath', 'qwerty', 'Surath Gunawardena'),
('U1560785951124', 'namali', 'namali1', 'Namali'),
('U1560784552125', 'suni', 'suni123', 'Sunimal'),
('U1560876369496', '1', '1', '1'),
('U1560877014704', '2', '2', '2'),
('U1560877077430', '21', '21', '2'),
('U1560878112563', 'isuru', 'isuru', 'isuru'),
('U1560878737529', 'banda', 'banda', 'abcbanda'),
('U1560879157848', 'hifriend', 'hifriend', 'hshshs'),
('U1560879500810', 'abc', 'abc', 'abc'),
('U1560880336868', 'charitha', 'charitha', 'charitha'),
('U1560881396833', '211', '211', '2');

-- --------------------------------------------------------

--
-- Table structure for table `offerride`
--

CREATE TABLE `offerride` (
  `OID` varchar(20) NOT NULL,
  `UserID` varchar(20) NOT NULL,
  `Source` varchar(255) NOT NULL,
  `Destination` varchar(255) NOT NULL,
  `StartDate` datetime NOT NULL,
  `StartTime` time NOT NULL,
  `WaitingTime` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `offerride`
--

INSERT INTO `offerride` (`OID`, `UserID`, `Source`, `Destination`, `StartDate`, `StartTime`, `WaitingTime`) VALUES
('O1560878656791', 'U1560784552125', 'malabe', 'kaduwela', '2019-06-20 00:00:00', '10:52:00', '5');

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
  `MotionSickness` varchar(20) NOT NULL,
  `LikeQuietness` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `preference`
--

INSERT INTO `preference` (`PID`, `UserID`, `GenderP`, `LanguageS`, `Smoking`, `MusicLover`, `MotionSickness`, `LikeQuietness`) VALUES
('PRF1560786053994', 'U1560785951124', 'Female', 'Sinhala', 'No', 'Yes', 'Yes', 'No'),
('PRF1560784742511', 'U1560784552125', 'No', 'Sinhala', 'No', 'Yes', 'No', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `rating_personal`
--

CREATE TABLE `rating_personal` (
  `tableID` int(20) NOT NULL,
  `TripId` varchar(50) NOT NULL,
  `UserID` varchar(255) NOT NULL,
  `UserType` varchar(50) NOT NULL,
  `RatedBy` varchar(255) NOT NULL,
  `GivenRating` varchar(20) NOT NULL,
  `CalculatedRating` varchar(20) NOT NULL,
  `AverageRating` varchar(20) NOT NULL,
  `Compliment` varchar(255) DEFAULT NULL,
  `Dissatisfaction` varchar(255) DEFAULT NULL,
  `Sentiment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rating_personal`
--

INSERT INTO `rating_personal` (`tableID`, `TripId`, `UserID`, `UserType`, `RatedBy`, `GivenRating`, `CalculatedRating`, `AverageRating`, `Compliment`, `Dissatisfaction`, `Sentiment`) VALUES
(2, 'T000001', 'U000001', 'driver', 'U00003', '4', '3', '3.5', NULL, NULL, NULL),
(3, 'T000001', 'U000001', 'driver', 'U00005', '3', '3', '3', NULL, NULL, NULL),
(4, 'T000001', 'U000002', 'driver', 'U00005', '3', '3', '3', NULL, NULL, NULL),
(5, 'T000005', 'U000002', 'driver', 'U00002', '5', '3', '4', NULL, NULL, NULL),
(7, 'T000005', 'U000002', 'passenger', 'U00003', '5', '3', '4', NULL, 'Professionalism', NULL),
(10, '00001', 'U000001', 'driver', 'U0000002', '3.0', '3.0', '3', NULL, 'Reckless Driving', '');

-- --------------------------------------------------------

--
-- Table structure for table `rating_vehicle`
--

CREATE TABLE `rating_vehicle` (
  `tableID` int(20) NOT NULL,
  `tripId` varchar(50) NOT NULL,
  `vehicleId` varchar(255) NOT NULL,
  `RatedBy` varchar(255) NOT NULL,
  `GivenRating` varchar(20) NOT NULL,
  `CalculatedRating` varchar(20) NOT NULL,
  `AverageRating` varchar(20) NOT NULL,
  `Dissatisfaction` varchar(255) DEFAULT NULL,
  `Sentiment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rating_vehicle`
--

INSERT INTO `rating_vehicle` (`tableID`, `tripId`, `vehicleId`, `RatedBy`, `GivenRating`, `CalculatedRating`, `AverageRating`, `Dissatisfaction`, `Sentiment`) VALUES
(9, '00001', 'V1560496428978', 'U0000002', '2.0', '2.0', '2', 'Comfortability', ''),
(11, '00001', 'V1560496428978', 'U0000002', '3.0', '3.0', '3', 'none', 'test sentiment '),
(12, '00001', 'V1560496428978', 'U0000002', '3.0', '3.0', '3', 'Comfortability', ''),
(13, '00001', 'V1560496428978', 'U0000002', '4.0', '4.0', '4', 'Vehicle Quality', '');

-- --------------------------------------------------------

--
-- Table structure for table `reported_drivers`
--

CREATE TABLE `reported_drivers` (
  `RID` varchar(20) NOT NULL,
  `PUID` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Passenger UID',
  `DUID` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Reported Driver''s UID'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `reported_drivers`
--

INSERT INTO `reported_drivers` (`RID`, `PUID`, `DUID`) VALUES
('1', '517011168906', '483075370677'),
('2', '517011168906', '81444871489');

-- --------------------------------------------------------

--
-- Table structure for table `searching_destination`
--

CREATE TABLE `searching_destination` (
  `UserID` varchar(20) NOT NULL,
  `StartingLoc` varchar(200) NOT NULL,
  `DestinationLoc` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `telephone_numbers`
--

CREATE TABLE `telephone_numbers` (
  `TelephoneID` varchar(20) NOT NULL,
  `Telephone` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `trip_requests`
--

CREATE TABLE `trip_requests` (
  `id` int(11) NOT NULL,
  `reqId` varchar(45) DEFAULT NULL,
  `tripId` varchar(45) DEFAULT NULL,
  `request_passenger` varchar(45) DEFAULT NULL,
  `request_driver` varchar(45) DEFAULT NULL,
  `pickup_location` varchar(45) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `destination` varchar(255) DEFAULT NULL,
  `req_accept` int(11) DEFAULT '0',
  `req_decline` int(11) DEFAULT '0',
  `token` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UserID` varchar(20) NOT NULL,
  `FullName` varchar(250) NOT NULL,
  `Profession` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Age` int(3) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `RName` varchar(255) NOT NULL,
  `RPhone` int(10) NOT NULL,
  `img` varchar(100) NOT NULL,
  `Token` varchar(1000) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UserID`, `FullName`, `Profession`, `Email`, `Age`, `Gender`, `RName`, `RPhone`, `img`, `Token`) VALUES
('U1560785951124', 'Namali Perera', 'HR', 'na12mali@gmail.com', 29, 'Female', 'Gagul Perera', 771755536, '/images/U1560785951124.jpg', NULL),
('U1560784552125', 'Sunimal Silva', 'Cashier', 'suni@yahoo.com', 31, 'Male', 'Darell Harper', 712846608, '/images/U1560784552125.jpg', NULL),
('U1560878737529', 'bada', 'Driver', 'bada@gmail.com', 2, 'Male', 'bada', 555555, '/images/null', NULL),
('U1560880336868', 'charitha', 'Driver', 'charitha@charitha.lk', 5, 'Male', 'charitha', 2688, '/images/null', NULL);

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
  `FrontView` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`VehicleID`, `UserID`, `Brand`, `Model`, `VNumber`, `Mileage`, `MYear`, `RYear`, `FuelType`, `TType`, `EngineCapacity`, `FrontView`) VALUES
('V1558286100676', 'U123456787', 'sdfghj', 'hj', '2345g', '100', '1990', 'i7', 'jk', 'sddfghj', '33456gfhhj', '456789'),
('V1560496428978', 'U1560496143004', 'Suzuki', 'Suzuki Goop', '1290uf', '120', '1980', '1980', 'Petrol', 'Auto', '1000cc', '/images/U1560496143004V.jpg'),
('V1560784772429', 'U1560784552125', 'Alto', 'Maruti Alto 800', 'CDA1212', '100', '1980', '1980', 'Petrol', 'Auto', '1000cc', '/images/U1560784552125V.jpg'),
('V1560786086727', 'U1560785951124', 'Alto', 'Maruti Alto 800', 'CFF8909', '200', '1980', '1980', 'Petrol', 'Auto', '1000cc', '/images/U1560785951124V.jpg');

-- --------------------------------------------------------

--
-- Stand-in structure for view `V_PERSONAL_RATING`
-- (See below for the actual view)
--
CREATE TABLE `V_PERSONAL_RATING` (
`UID` varchar(255)
,`Rating` double(22,2)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `V_VEHICLE_RATING`
-- (See below for the actual view)
--
CREATE TABLE `V_VEHICLE_RATING` (
`vehicleID` varchar(255)
,`userID` varchar(255)
,`vehiclerating` double(22,2)
);

-- --------------------------------------------------------

--
-- Structure for view `V_PERSONAL_RATING`
--
DROP TABLE IF EXISTS `V_PERSONAL_RATING`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cdapadmin`@`%` SQL SECURITY DEFINER VIEW `V_PERSONAL_RATING`  AS  select `rp`.`UserID` AS `UID`,round(avg(`rp`.`AverageRating`),2) AS `Rating` from `rating_personal` `rp` group by `rp`.`UserID` ;

-- --------------------------------------------------------

--
-- Structure for view `V_VEHICLE_RATING`
--
DROP TABLE IF EXISTS `V_VEHICLE_RATING`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cdapadmin`@`%` SQL SECURITY DEFINER VIEW `V_VEHICLE_RATING`  AS  select `rv`.`vehicleId` AS `vehicleID`,`v`.`UserID` AS `userID`,round(avg(`rv`.`AverageRating`),2) AS `vehiclerating` from (`rating_vehicle` `rv` join `vehicle` `v`) where (`rv`.`vehicleId` = `v`.`VehicleID`) group by `v`.`VehicleID` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `current_passengers`
--
ALTER TABLE `current_passengers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `offerride`
--
ALTER TABLE `offerride`
  ADD PRIMARY KEY (`OID`),
  ADD KEY `UserID` (`UserID`);

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
-- Indexes for table `rating_personal`
--
ALTER TABLE `rating_personal`
  ADD PRIMARY KEY (`tableID`);

--
-- Indexes for table `rating_vehicle`
--
ALTER TABLE `rating_vehicle`
  ADD PRIMARY KEY (`tableID`);

--
-- Indexes for table `reported_drivers`
--
ALTER TABLE `reported_drivers`
  ADD PRIMARY KEY (`RID`);

--
-- Indexes for table `telephone_numbers`
--
ALTER TABLE `telephone_numbers`
  ADD PRIMARY KEY (`TelephoneID`);

--
-- Indexes for table `trip_requests`
--
ALTER TABLE `trip_requests`
  ADD PRIMARY KEY (`id`);

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

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `current_passengers`
--
ALTER TABLE `current_passengers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rating_personal`
--
ALTER TABLE `rating_personal`
  MODIFY `tableID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `rating_vehicle`
--
ALTER TABLE `rating_vehicle`
  MODIFY `tableID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `trip_requests`
--
ALTER TABLE `trip_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
