-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and store
-- the average weighted score for all students.
DELIMITER //


CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE user_id INT;
	DECLARE total_score FLOAT;
	DECLARE total_weight INT;
	DECLARE average_score FLOAT;

	-- Cursor to iterate over the users
	DECLARE cur CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	OPEN cur;

	read_loop: LOOP
		FETCH cur INTO user_id;
		IF done THEN
			LEAVE read_loop;
		END IF;

		SELECT SUM(c.score * p.weight), SUM(p.weight)
		INTO total_score, total_weight
		FROM corrections c
		INNER JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = user_id;

		IF total_weight > 0 THEN
			SET average_score = total_score / total_weight;
		ELSE 
			SET average_score = 0;
		END IF;

		UPDATE users
		SET average_score = average_score
		WHERE id = user_id;
	END LOOP;

	CLOSE cur;
END //


DELIMITER ;

