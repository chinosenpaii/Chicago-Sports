-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Apr 21, 2022 at 11:06 PM
-- Server version: 5.7.34
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `353Project`
--

-- --------------------------------------------------------

--
-- Table structure for table `Matches`
--

CREATE TABLE `Matches` (
  `matchID` varchar(20) NOT NULL,
  `score` int(11) NOT NULL,
  `arena` varchar(15) NOT NULL,
  `matchType` varchar(15) NOT NULL,
  `status` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `teamName` varchar(40) NOT NULL,
  `oppName` varchar(40) NOT NULL,
  `sport` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Opponent`
--

CREATE TABLE `Opponent` (
  `oppName` varchar(40) NOT NULL,
  `leagueName` varchar(20) NOT NULL,
  `sport` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Opponent`
--

INSERT INTO `Opponent` (`oppName`, `leagueName`, `sport`) VALUES
('Anaheim Ducks', 'NHL', 'Hockey'),
('Arizona Cardinals', 'NFL', 'Football'),
('Arizona Coyotes', 'NHL', 'Hockey'),
('Arizona Diamondbacks', 'MLB', 'Baseball'),
('Atlanta', 'Falcons', 'Football'),
('Atlanta Braves', 'MLB', 'Baseball'),
('Atlanta Hawks', 'NBA', 'Basketball'),
('Atlanta United', 'MLS', 'Soccer'),
('Austin FC', 'MLS', 'Soccer'),
('Baltimore Orioles', 'MLB', 'Baseball'),
('Baltimore Ravens', 'NFL', 'Football'),
('Boston Bruins', 'NHL', 'Hockey'),
('Boston Celtics', 'NBA', 'Basketball'),
('Boston Red Sox', 'MLB', 'Baseball'),
('Brooklyn Nets', 'NBA', 'Basketball'),
('Buffalo Bills', 'NFL', 'Football'),
('Buffalo Sabres', 'NHL', 'Hockey'),
('Calgary Flames', 'NHL', 'Hockey'),
('Carolina Hurricanes', 'NHL', 'Hockey'),
('Carolina Panthers', 'NFL', 'Football'),
('CF Montreal', 'MLS', 'Soccer'),
('Charlotte FC', 'MLS', 'Soccer'),
('Charlotte Hornets', 'NBA', 'Basketball'),
('Chicago Cubs', 'MLB', 'Baseball'),
('Chicago White Sox', 'MLB', 'Baseball'),
('Cincinnati Bengals', 'NFL', 'Football'),
('Cincinnati Reds', 'MLB', 'Baseball'),
('Cleveland Browns', 'NFL', 'Football'),
('Cleveland Cavaliers', 'NBA', 'Basketball'),
('Cleveland Guardians', 'MLB', 'Baseball'),
('Colorado Avalanche', 'NHL', 'Hockey'),
('Colorado Rapids', 'MLS', 'Soccer'),
('Colorado Rockies', 'MLB', 'Baseball'),
('Columbus Blue Jackets', 'NHL', 'Hockey'),
('Columbus Crew', 'MLS', 'Soccer'),
('D.C. United', 'MLS', 'Soccer'),
('Dallas Cowboys', 'NFL', 'Football'),
('Dallas Mavericks', 'NBA', 'Basketball'),
('Dallas Stars', 'NHL', 'Hockey'),
('Denver Broncos', 'NFL', 'Football'),
('Denver Nuggets', 'NBA', 'Basketball'),
('Detroit Lions', 'NFL', 'Football'),
('Detroit Pistons', 'NBA', 'Basketball'),
('Detroit Red Wings', 'NHL', 'Hockey'),
('Detroit Tigers', 'MLB', 'Baseball'),
('Edmonton Oilers', 'NHL', 'Hockey'),
('FC Cincinnati', 'MLS', 'Soccer'),
('FC Dallas', 'MLS', 'Soccer'),
('Florida Panthers', 'NHL', 'Hockey'),
('Golden State Warriors', 'NBA', 'Basketball'),
('Green Bay Packers', 'NFL', 'Football'),
('Houston Astros', 'MLB', 'Baseball'),
('Houston Dynamo FC', 'MLS', 'Soccer'),
('Houston Rockets', 'NBA', 'Basketball'),
('Houston Texans', 'NFL', 'Football'),
('Indiana Pacers', 'NBA', 'Basketball'),
('Indianapolis Colts', 'NFL', 'Football'),
('Inter Miami CF', 'MLS', 'Soccer'),
('Jacksonville Jaguars', 'NFL', 'Football'),
('Kansas City Chiefs', 'NFL', 'Football'),
('Kansas City Royals', 'MLB', 'Baseball'),
('LA Clippers', 'NBA', 'Basketball'),
('LA Galaxy', 'MLS', 'Soccer'),
('Las Vegas Raiders', 'NFL', 'Football'),
('Los Angeles Angels', 'MLB', 'Baseball'),
('Los Angeles Chargers', 'NFL', 'Football'),
('Los Angeles Dodgers', 'MLB', 'Baseball'),
('Los Angeles Football Club', 'MLS', 'Soccer'),
('Los Angeles Kings', 'NHL', 'Hockey'),
('Los Angeles Lakers', 'NBA', 'Basketball'),
('Los Angeles Rams', 'NFL', 'Football'),
('Memphis Grizzlies', 'NBA', 'Basketball'),
('Miami Dolphins', 'NFL', 'Football'),
('Miami Heat', 'NBA', 'Basketball'),
('Miami Marlins', 'MLB', 'Baseball'),
('Milwaukee Brewers', 'MLB', 'Baseball'),
('Milwaukee Bucks', 'NBA', 'Basketball'),
('Minnesota Timberwolves', 'NBA', 'Basketball'),
('Minnesota Twins', 'MLB', 'Baseball'),
('Minnesota United', 'MLS', 'Soccer'),
('Minnesota Vikings', 'NFL', 'Football'),
('Minnesota Wild', 'NHL', 'Hockey'),
('Montreal Canadiens', 'NHL', 'Hockey'),
('Nashville Predators', 'NHL', 'Hockey'),
('Nashville SC', 'MLS', 'Soccer'),
('New England Patriots', 'NFL', 'Football'),
('New England Revolution', 'MLS', 'Soccer'),
('New Jersey Devils', 'NHL', 'Hockey'),
('New Orleans Pelicans', 'NBA', 'Basketball'),
('New Orleans Saints', 'NFL', 'Football'),
('New York City FC', 'MLS', 'Soccer'),
('New York Giants', 'NFL', 'Football'),
('New York Islanders', 'NHL', 'Hockey'),
('New York Jets', 'NFL', 'Football'),
('New York Knicks', 'NBA', 'Basketball'),
('New York Mets', 'MLB', 'Baseball'),
('New York Rangers', 'NHL', 'Hockey'),
('New York Red Bulls', 'MLS', 'Soccer'),
('New York Yankees', 'MLB', 'Baseball'),
('Oakland Athletics', 'MLB', 'Baseball'),
('Oklahoma City Thunder', 'NBA', 'Basketball'),
('Orlando City', 'MLS', 'Soccer'),
('Orlando Magic', 'NBA', 'Basketball'),
('Ottawa Senators', 'NHL', 'Hockey'),
('Philadelphia 76ers', 'NBA', 'Basketball'),
('Philadelphia Eagles', 'NFL', 'Football'),
('Philadelphia Flyers', 'NHL', 'Hockey'),
('Philadelphia Phillies', 'MLB', 'Baseball'),
('Philadelphia Union', 'MLS', 'Soccer'),
('Phoenix Suns', 'NBA', 'Basketball'),
('Pittsburgh Penguins', 'NHL', 'Hockey'),
('Pittsburgh Pirates', 'MLB', 'Baseball'),
('Pittsburgh Steelers', 'NFL', 'Football'),
('Portland Timbers', 'MLS', 'Soccer'),
('Portland Trail Blazers', 'NBA', 'Basketball'),
('Real Salt Lake', 'MLS', 'Soccer'),
('Sacramento Kings', 'NBA', 'Basketball'),
('San Antonio Spurs', 'NBA', 'Basketball'),
('San Diego Padres', 'MLB', 'Baseball'),
('San Francisco 49ers', 'NFL', 'Football'),
('San Francisco Giants', 'MLB', 'Baseball'),
('San Jose Earthquakes', 'MLS', 'Soccer'),
('San Jose Sharks', 'NHL', 'Hockey'),
('Seattle Kraken', 'NHL', 'Hockey'),
('Seattle Mariners', 'MLB', 'Baseball'),
('Seattle Seahawks', 'NFL', 'Football'),
('Seattle Sounders FC', 'MLS', 'Soccer'),
('Sporting Kansas City', 'MLS', 'Soccer'),
('St. Louis Blues', 'NHL', 'Hockey'),
('St. Louis Cardinals', 'MLB', 'Baseball'),
('Tampa Bay Buccaneers', 'NFL', 'Football'),
('Tampa Bay Lightning', 'NHL', 'Hockey'),
('Tampa Bay Rays', 'MLB', 'Baseball'),
('Tennessee Titans', 'NFL', 'Football'),
('Texas Rangers', 'MLB', 'Baseball'),
('Toronto Blue Jays', 'MLB', 'Baseball'),
('Toronto FC', 'MLS', 'Soccer'),
('Toronto Maple Leafs', 'NHL', 'Hockey'),
('Toronto Raptors', 'NBA', 'Basketball'),
('Utah Jazz', 'NBA', 'Basketball'),
('Vancouver Canucks', 'NHL', 'Hockey'),
('Vancouver Whitecaps FC', 'MLS', 'Soccer'),
('Vegas Golden Knights', 'NHL', 'Hockey'),
('Washington Capitals', 'NHL', 'Hockey'),
('Washington Commanders', 'NFL', 'Football'),
('Washington Nationals', 'MLB', 'Baseball'),
('Washington Wizards', 'NBA', 'Basketball'),
('Winnipeg Jets', 'NHL', 'Hockey');

-- --------------------------------------------------------

--
-- Table structure for table `Sport`
--

CREATE TABLE `Sport` (
  `sportName` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Sport`
--

INSERT INTO `Sport` (`sportName`) VALUES
('Baseball'),
('Basketball'),
('Football'),
('Hockey'),
('Soccer');

-- --------------------------------------------------------

--
-- Table structure for table `Team`
--

CREATE TABLE `Team` (
  `teamName` varchar(40) NOT NULL,
  `leagueName` varchar(20) NOT NULL,
  `sport` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Team`
--

INSERT INTO `Team` (`teamName`, `leagueName`, `sport`) VALUES
('Chicago Bears', 'NFL', 'Football'),
('Chicago Blackhawks', 'NHL', 'Hockey'),
('Chicago Bulls', 'NBA', 'Basketball'),
('Chicago Cubs', 'MLB', 'Baseball'),
('Chicago Fire', 'MLS', 'Soccer'),
('Chicago White Sox', 'MLB', 'Baseball');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `UserID` varchar(5) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`UserID`, `password`) VALUES
('admin', 'Chicago6!');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Matches`
--
ALTER TABLE `Matches`
  ADD PRIMARY KEY (`matchID`),
  ADD KEY `teamName` (`teamName`),
  ADD KEY `oppName` (`oppName`),
  ADD KEY `sport` (`sport`);

--
-- Indexes for table `Opponent`
--
ALTER TABLE `Opponent`
  ADD PRIMARY KEY (`oppName`),
  ADD KEY `sport` (`sport`);

--
-- Indexes for table `Sport`
--
ALTER TABLE `Sport`
  ADD PRIMARY KEY (`sportName`);

--
-- Indexes for table `Team`
--
ALTER TABLE `Team`
  ADD PRIMARY KEY (`teamName`),
  ADD KEY `sport` (`sport`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`UserID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Matches`
--
ALTER TABLE `Matches`
  ADD CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`teamName`) REFERENCES `Team` (`teamName`),
  ADD CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`oppName`) REFERENCES `Opponent` (`oppName`),
  ADD CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`sport`) REFERENCES `Sport` (`sportName`);

--
-- Constraints for table `Opponent`
--
ALTER TABLE `Opponent`
  ADD CONSTRAINT `opponent_ibfk_1` FOREIGN KEY (`sport`) REFERENCES `Sport` (`sportName`);

--
-- Constraints for table `Team`
--
ALTER TABLE `Team`
  ADD CONSTRAINT `team_ibfk_1` FOREIGN KEY (`sport`) REFERENCES `Sport` (`sportName`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
