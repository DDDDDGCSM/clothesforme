-- 修复昨天的衣服数据：将昨天被误标记为 'book' 的数据改回 'clothes'
-- 注意：这个脚本假设昨天的数据应该是 'clothes' 类型
-- 执行前请先备份数据库！

-- 方法1：如果确定昨天（2026-01-11）的所有数据都是衣服数据，执行：
UPDATE book_exchange_events 
SET project_type = 'clothes' 
WHERE DATE(created_at) = '2026-01-11' 
  AND project_type = 'book';

-- 方法2：如果只想修复特定日期范围的数据，执行：
-- UPDATE book_exchange_events 
-- SET project_type = 'clothes' 
-- WHERE DATE(created_at) >= '2026-01-11' 
--   AND DATE(created_at) < '2026-01-12'
--   AND project_type = 'book';

-- 查看修复结果：
-- SELECT DATE(created_at) as day, project_type, COUNT(*) as count
-- FROM book_exchange_events
-- WHERE DATE(created_at) >= '2026-01-11'
-- GROUP BY day, project_type
-- ORDER BY day DESC;

