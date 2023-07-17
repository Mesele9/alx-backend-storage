-- SQL script that creates a stored procedure 
-- ComputeAverageWeightedScoreForUser that computes and store
-- the average weighted score for a student.
DELIMITER //


CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT;
	DECLARE total_weight FLOAT;
	DECLARE average_score FLOAT;

	SELECT SUM(c.score * p.weight), SUM(p.weight)
	INTO total_score, total_weight
	FROM corrections c
	JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	SET average_score = IF(total_weight > 0, total_score / total_weight, 0);

	UPDATE users
	SET average_score = average_score
	WHERE id - user_id;
END //


DELIMITER ;
