-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2020 at 06:36 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tinder`
--

-- --------------------------------------------------------

--
-- Table structure for table `proposals`
--

CREATE TABLE `proposals` (
  `proposal_id` int(11) NOT NULL,
  `romeo_id` int(11) NOT NULL,
  `juliet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `proposals`
--

INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES
(6, 10, 8),
(8, 1, 10),
(9, 12, 10),
(10, 1, 6),
(11, 14, 11),
(12, 14, 12),
(13, 10, 1),
(15, 13, 1),
(16, 1, 5),
(17, 23, 8),
(18, 23, 11),
(19, 23, 12),
(20, 1, 24),
(21, 24, 1),
(22, 24, 8),
(23, 24, 9),
(24, 5, 1),
(25, 5, 11),
(26, 5, 12),
(27, 5, 17),
(28, 5, 25),
(29, 11, 5),
(30, 11, 6),
(31, 11, 10),
(32, 11, 13),
(33, 6, 11),
(34, 6, 12),
(35, 6, 17),
(36, 6, 18),
(37, 1, 13),
(38, 1, 19),
(39, 23, 1),
(40, 1, 7),
(41, 1, 26),
(42, 28, 1),
(43, 28, 9),
(44, 28, 11),
(45, 1, 28),
(46, 29, 1),
(47, 30, 5),
(48, 5, 9);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `age` int(3) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `bg` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `bio` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `fname`, `email`, `password`, `age`, `gender`, `bg`, `city`, `bio`) VALUES
(1, 'Ananya Roy', 'ananya@gmail.com', 'abcd', 21, 'Female', 'Avatar.jpg', 'Chandannagar', 'Engineering student'),
(5, 'Rohit Sharma', 'rohit@gmail.com', '12345', 33, 'Male', 'Avatar.jpg', 'Mumbai', 'Indian Cricketer'),
(6, 'Shah Rukh Khan', 'shahrukh@rediffmail.com', 'srk', 54, 'Male', 'srk.jpg', 'Mumbai', 'King Khan'),
(7, 'Donald Trump', 'donald@gmail.com', 'USA', 65, 'Male', 'Avatar.jpg', 'New York', 'President of US'),
(8, 'Deepika Padukone', 'dp@gmail.com', 'ranveer', 34, 'Female', 'Avatar.jpg', 'Bangalore', 'Actress'),
(9, 'Kate Winslet', 'kate@gmail.com', 'abcd', 44, 'Female', 'k.jpg', 'San Fransisco', 'Hollywood Actress'),
(10, 'Tom Cruise', 'tomcruise@gmail.com', 'abcd', 56, 'Male', 'Avatar.jpg', 'New York', 'Hollywood actor'),
(11, 'Katrina Kaif', 'kaif@gmail.com', '1234', 36, 'Female', 'Avatar.jpg', 'Mumbai', 'Bollywood actress'),
(12, 'Taylor Swift', 'swift@rediffmail.com', 'taylor', 32, 'Female', 'Avatar.jpg', 'New York', 'Play-back singer'),
(13, 'Shane Warne', 'warne@gmail.com', 'abcd', 49, 'Male', 'Avatar.jpg', 'Sydney', 'Australian Cricketer'),
(14, 'Salman Khan', 'beinghuman@gmail.com', 'blackbuck', 54, 'Male', 'Avatar.jpg', 'Mumbai', 'Bollywood Actor'),
(15, 'Narendra Modi', 'acchedin@gmail.com', 'abcd', 68, 'Male', 'Avatar.jpg', 'Ahmedabad', 'PM of India'),
(17, 'Lara Dutta', 'dutta@gmail.com', 'abcd', 42, 'Female', 'Avatar.jpg', 'Mumbai', 'Actress'),
(18, 'PV Sindhu', 'sindhu@gmail.com', 'abcd', 25, 'Female', 'Avatar.jpg', 'Hyderabad', 'Badminton player'),
(19, 'Roger Federer', 'fed@gmail.com', 'abcd', 34, 'Male', 'Avatar.jpg', 'Lisbon', 'Tennis player'),
(23, 'Sunil Chetri', 'chetri@gmail.com', 'abcd', 33, 'Male', 'Avatar.jpg', 'Kolkata', 'Footballer'),
(24, 'Bhuvam Bam', 'bb@gmail.com', 'abcd', 26, 'Male', 'Avatar.jpg', 'Delhi', 'Youtuber'),
(25, 'Maria Sharapova', 'sha@gmail.com', 'tennis', 32, 'Female', 'Avatar.jpg', 'Moscow', 'Tennis Player'),
(26, 'Leander Paes', 'paes@gmail.com', 'abcd', 45, 'Male', 'Avatar.jpg', 'Chennai', 'Tennis Player'),
(27, 'Akshay Kumar', 'akki@gmail.com', 'abcd', 50, 'Male', 'Avatar.jpg', 'Mumbai', 'Bollywood actor'),
(28, 'Vikas Khanna', 'khanna@rediffmail.com', 'chef', 36, 'Male', 'Avatar.jpg', 'Chandigarh', 'Celebrity Chef'),
(29, 'Ayushman Khurrana', 'ayush@gmail.com', 'abcd', 33, 'Male', 'Avatar.jpg', 'Delhi', 'Actor'),
(30, 'Mithali Raj', 'mithali@gmail.com', 'cricket', 37, 'Female', 'Avatar.jpg', 'Banaglore', 'Indian cricketer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proposals`
--
ALTER TABLE `proposals`
  ADD PRIMARY KEY (`proposal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `proposals`
--
ALTER TABLE `proposals`
  MODIFY `proposal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
