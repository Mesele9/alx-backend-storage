-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. 
DELIMITER //


CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;

	-- Compute average score
	SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;

	-- update the average_score column for theuser
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END //


DELIMITER ;
