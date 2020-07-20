-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 20, 2020 at 09:28 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment35`
--

-- --------------------------------------------------------

--
-- Table structure for table `t1`
--

CREATE TABLE `t1` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `t1`
--

INSERT INTO `t1` (`id`, `name`, `address`) VALUES
(1, 'Peter', 'Lowstreet 4'),
(2, 'Amy', 'Apple st 652'),
(3, 'Hannah', 'Mountain 21'),
(4, 'Michael', 'Valley 345'),
(5, 'Sandy', 'Ocean blvd 2'),
(6, 'Betty', 'Green Grass 1'),
(7, 'Richard', 'Sky st 331'),
(8, 'Susan', 'One way 98'),
(9, 'Vicky', 'Yellow Garden 2'),
(10, 'Ben', 'Park Lane 38'),
(11, 'William', 'Central st 954'),
(12, 'Chuck', 'Main Road 989'),
(13, 'Viola', 'Sideway 1633');

-- --------------------------------------------------------

--
-- Table structure for table `t2`
--

CREATE TABLE `t2` (
  `id` int(11) NOT NULL,
  `enrollment_number` varchar(255) DEFAULT NULL,
  `Semester` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `t2`
--

INSERT INTO `t2` (`id`, `enrollment_number`, `Semester`) VALUES
(1, '17SE02CE010', '6'),
(2, '17SE02CE011', '7'),
(3, '17SE02CE012', '5'),
(4, '17SE02CE013', '4'),
(5, '17SE02CE014', '3'),
(6, '17SE02CE015', '2'),
(7, '17SE02CE016', '1'),
(8, '17SE02CE017', '8'),
(9, '17SE02CE018', '5'),
(10, '17SE02CE019', '6'),
(11, '17SE02CE020', '4'),
(12, '17SE02CE021', '3'),
(13, '17SE02CE022', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `t1`
--
ALTER TABLE `t1`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `t2`
--
ALTER TABLE `t2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `t1`
--
ALTER TABLE `t1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `t2`
--
ALTER TABLE `t2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
