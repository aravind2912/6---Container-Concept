CREATE TABLE Students (
  RegNo INT NOT NULL,
  Name VARCHAR(255) NOT NULL,
  Vaccination_Status VARCHAR(3),
  PRIMARY KEY (RegNo)
);

INSERT INTO Students (RegNo, Name, Vaccination_Status)
VALUES
  (1, 'John', 'Yes'),
  (2, 'Mary', 'No'),
  (3, 'Peter', 'Yes'),
  (4, 'Sarah', 'No');
