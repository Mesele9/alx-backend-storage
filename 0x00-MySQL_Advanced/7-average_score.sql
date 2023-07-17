-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. 
DELIMITER //


CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE average_score FLOAT;
	DECLARE num_corrections INT;
	DECLARE total_score FLOAT;

	-- Compute total score for a user
	SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;

	-- compute the number of corrections
	SELECT COUNT(*) INTO num_corrections FROM corrections WHERE user_id = user_id;

	-- Compute average score
	IF num_corrections > 0 THEN
		SET average_score = total_score / num_corrections;
	ELSE 
		SET average_score = 0;
	END IF;

	-- update the average_score column for theuser
	UPDATE users SET average_score = average_score WHERE id = user_id;
END //


DELIMITER ;
