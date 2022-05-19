-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-05-2022 a las 02:17:05
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `ID_cliente` int(50) NOT NULL,
  `nombre_cliente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email_cliente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tel_cliente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ultima_modificacion` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`ID_cliente`, `nombre_cliente`, `email_cliente`, `tel_cliente`, `ultima_modificacion`) VALUES
(2, 'Anyel', 'anyel@gmail', '54655464', 'Keyli Lorena'),
(3, 'Rafael', 'kshdsdhs', '54645', 'Lazaro Altedill Hernandez');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `ID_equipo` int(50) NOT NULL,
  `ID_cliente` int(50) NOT NULL,
  `marca` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tipo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `modelo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `observaciones_capturista` text COLLATE utf8_unicode_ci NOT NULL,
  `estatus` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`ID_equipo`, `ID_cliente`, `marca`, `tipo`, `modelo`, `observaciones_capturista`, `estatus`) VALUES
(8, 2, 'hp', 'Laptop', 'asd', 'dasdafafaffffdf\n', 'Nuevo Ingreso'),
(9, 2, 'd', 'Desktop', 'd', 'd\n', 'Nuevo Ingreso'),
(12, 2, 'w', 'Tablet', 'www', 'w\n', 'Nuevo Ingreso'),
(13, 2, 'Asus', 'Laptop', 'asusgtx', 'sin teclas\n', 'Nuevo Ingreso'),
(22, 2, 'qewe', 'Laptop', 'eee', 'ee\n', 'Nuevo Ingreso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `ID` int(50) NOT NULL,
  `nombre_usuario` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `pass` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `permisos` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `estatus` varchar(50) CHARACTER SET utf32 COLLATE utf32_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nombre_completo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` int(50) NOT NULL,
  `registrado_por` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`ID`, `nombre_usuario`, `pass`, `permisos`, `estatus`, `email`, `nombre_completo`, `telefono`, `registrado_por`) VALUES
(1, 'lazaro', '1234', 'Administrador', 'Activo', 'lazaro@nauta.cu', 'Lazaro Altedill Hernandez', 54499848, ''),
(47, 'key', '123', 'Capturista', 'Activo', 'key@gmail.com', 'Keyli Lorena', 54943864, ''),
(48, 'yuli', '123', 'Tecnico', 'Activo', 'yuli@gmail.com', 'Yulennis', 54681213, 'Lazaro Altedill Hernandez'),
(50, 'sd', 'sd', 'Tecnico', 'Activo', 'adad', 'asd', 0, 'Lazaro Altedill Hernandez'),
(51, 'asd', '1', 'Tecnico', 'Inactivo', 'asdasd@gmail', 'lazaroah', 466651, 'Lazaro Altedill Hernandez'),
(52, 'yor', '1234', 'Capturista', 'Activo', 'lsadasd', 'Yorlay', 54655, 'Lazaro Altedill Hernandez');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID_cliente`);

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`ID_equipo`,`ID_cliente`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ID_cliente` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `ID_equipo` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
