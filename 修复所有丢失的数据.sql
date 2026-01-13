-- ============================================
-- 修复所有丢失的衣服数据
-- ============================================
-- 问题：之前的数据库初始化逻辑将数据误标记为 'book'，导致数据丢失
-- 解决方案：将所有被误标记为 'book' 的数据改回 'clothes'
-- 
-- ⚠️ 执行前请先备份数据库！
-- ============================================

-- 步骤1：查看当前数据分布（按日期和项目类型）
-- 执行这个查询，看看有多少数据被误标记了
SELECT 
    DATE(created_at) as day,
    project_type,
    event_type,
    COUNT(*) as count
FROM book_exchange_events
WHERE DATE(created_at) >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY day, project_type, event_type
ORDER BY day DESC, project_type, event_type;

-- 步骤2：查看被误标记为 'book' 的数据总数
SELECT 
    DATE(created_at) as day,
    event_type,
    COUNT(*) as count
FROM book_exchange_events
WHERE project_type = 'book'
  AND DATE(created_at) >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY day, event_type
ORDER BY day DESC;

-- 步骤3：修复所有被误标记的数据
-- ⚠️ 重要：由于衣服项目是最近才开始的，所有最近的数据都应该是 'clothes'
-- 执行以下SQL将最近30天的所有 'book' 数据改回 'clothes'

UPDATE book_exchange_events 
SET project_type = 'clothes' 
WHERE project_type = 'book'
  AND DATE(created_at) >= CURRENT_DATE - INTERVAL '30 days';

-- 如果上面的修复不够，可以修复所有数据（谨慎使用）：
-- UPDATE book_exchange_events 
-- SET project_type = 'clothes' 
-- WHERE project_type = 'book';

-- 步骤4：验证修复结果
-- 执行后应该看到所有数据都是 'clothes' 类型
SELECT 
    DATE(created_at) as day,
    project_type,
    event_type,
    COUNT(*) as count
FROM book_exchange_events
WHERE DATE(created_at) >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY day, project_type, event_type
ORDER BY day DESC, project_type, event_type;

-- 步骤5：查看总体统计（修复后应该只有 'clothes' 类型）
SELECT 
    project_type,
    event_type,
    COUNT(*) as total_count
FROM book_exchange_events
WHERE DATE(created_at) >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY project_type, event_type
ORDER BY project_type, event_type;

-- 步骤6：查看修复后的总数据量（应该恢复到40+）
SELECT 
    DATE(created_at) as day,
    COUNT(*) as total_events,
    COUNT(DISTINCT ip) as unique_ips
FROM book_exchange_events
WHERE project_type = 'clothes'
  AND DATE(created_at) >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY day
ORDER BY day DESC;

