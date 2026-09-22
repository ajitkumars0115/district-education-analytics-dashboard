-- ==============================================
-- District Education Analytics Dashboard
-- SQL Analysis Queries
-- ==============================================

-- 1. Total number of schools in the district
SELECT COUNT(*) AS Total_Schools
FROM SchoolDetails;

-- 2. Block-wise school count (highest to lowest)
SELECT [Block Name], COUNT(*) AS School_Count
FROM SchoolDetails
GROUP BY [Block Name]
ORDER BY School_Count DESC;

-- 3. Rural vs Urban school distribution
SELECT [Location Type], COUNT(*) AS School_Count
FROM SchoolDetails
GROUP BY [Location Type]
ORDER BY School_Count DESC;

-- 4. Management type distribution (Govt/Private/Aided)
SELECT [Management Name], COUNT(*) AS School_Count
FROM SchoolDetails
GROUP BY [Management Name]
ORDER BY School_Count DESC;

-- 5. School category distribution (Primary/Upper Primary/Higher Secondary)
SELECT [School Category Name], COUNT(*) AS School_Count
FROM SchoolDetails
GROUP BY [School Category Name]
ORDER BY School_Count DESC;

-- 6. Medium of instruction distribution
SELECT [Medium of Instruction Names], COUNT(*) AS School_Count
FROM SchoolDetails
GROUP BY [Medium of Instruction Names]
ORDER BY School_Count DESC;

-- 7. Operational status (Active vs Permanently Closed)
SELECT [Operational Status], COUNT(*) AS School_Count
FROM SchoolDetails
GROUP BY [Operational Status]
ORDER BY School_Count DESC;

-- 8. Block-wise count of permanently closed schools
SELECT [Block Name], COUNT(*) AS Closed_Schools
FROM SchoolDetails
WHERE [Operational Status] = 'Permanently Closed'
GROUP BY [Block Name]
ORDER BY Closed_Schools DESC;
