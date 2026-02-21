"""
Database optimization script
Adds indexes and optimizes SQLite database for better performance
"""
from app import app
from models import db

def optimize_database():
    """Add indexes and optimize database"""
    with app.app_context():
        print("Optimizing database...")
        
        # Create composite indexes if they don't exist
        try:
            print("Creating composite indexes...")
            db.session.execute(db.text("""
                CREATE INDEX IF NOT EXISTS idx_province_district 
                ON people (province, district)
            """))
            
            db.session.execute(db.text("""
                CREATE INDEX IF NOT EXISTS idx_gender_age 
                ON people (gender, age)
            """))
            
            db.session.execute(db.text("""
                CREATE INDEX IF NOT EXISTS idx_name_province 
                ON people (name, province)
            """))
            
            db.session.commit()
            print("✓ Composite indexes created")
        except Exception as e:
            print(f"Note: {e}")
        
        # SQLite optimizations
        print("\nApplying SQLite optimizations...")
        
        # Enable WAL mode for better concurrency
        db.session.execute(db.text("PRAGMA journal_mode=WAL"))
        print("✓ WAL mode enabled")
        
        # Optimize synchronous mode
        db.session.execute(db.text("PRAGMA synchronous=NORMAL"))
        print("✓ Synchronous mode optimized")
        
        # Increase cache size (10MB)
        db.session.execute(db.text("PRAGMA cache_size=10000"))
        print("✓ Cache size increased")
        
        # Use memory for temp storage
        db.session.execute(db.text("PRAGMA temp_store=MEMORY"))
        print("✓ Temp storage set to memory")
        
        # Analyze database for query optimization
        print("\nAnalyzing database...")
        db.session.execute(db.text("ANALYZE"))
        db.session.commit()
        print("✓ Database analyzed")
        
        # Vacuum to reclaim space and optimize
        print("\nVacuuming database (this may take a while)...")
        db.session.execute(db.text("VACUUM"))
        print("✓ Database vacuumed")
        
        print("\n" + "="*50)
        print("DATABASE OPTIMIZATION COMPLETE!")
        print("="*50)
        print("\nPerformance improvements:")
        print("✓ Composite indexes for common queries")
        print("✓ WAL mode for better concurrency")
        print("✓ Optimized cache and synchronous settings")
        print("✓ Database analyzed and vacuumed")
        print("\nYour searches should now be much faster!")

if __name__ == '__main__':
    optimize_database()
