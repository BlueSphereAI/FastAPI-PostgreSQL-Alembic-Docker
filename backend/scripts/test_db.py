#!/usr/bin/env python3
"""
Script to test database connection and models.
"""
import asyncio
import uuid
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.database.user.model import User, UserType
from app.database.trainer.model import Trainer
from app.database.appointment.model import Appointment, AppointmentStatus
from app.database.feedback.model import Feedback
from app.database.availability.model import Availability
from app.config import get_settings

settings = get_settings()

# Create async engine
engine = create_async_engine(settings.PG_DATABASE_URL)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def test_database():
    """Test database connection and models."""
    print("Testing database connection and models...")
    
    async with async_session() as session:
        # Create a client user
        client_user = User(
            username="testclient",
            email="client@example.com",
            password_hash=User.create_password_hash("password123"),
            first_name="Test",
            last_name="Client",
            user_type=UserType.CLIENT
        )
        
        # Create a trainer user
        trainer_user = User(
            username="testtrainer",
            email="trainer@example.com",
            password_hash=User.create_password_hash("password123"),
            first_name="Test",
            last_name="Trainer",
            user_type=UserType.TRAINER
        )
        
        # Save users to database
        await client_user.save(session)
        await trainer_user.save(session)
        
        print(f"Created client user with UUID: {client_user.uuid}")
        print(f"Created trainer user with UUID: {trainer_user.uuid}")
        
        # Create trainer profile
        trainer = Trainer(
            user_id=trainer_user.uuid,
            biography="Experienced fitness trainer specializing in strength training.",
            certifications="ACE Certified Personal Trainer",
            hourly_rate=45.0,
            specialties="Strength training, Weight loss, Nutrition",
            location="New York, NY"
        )
        
        # Save trainer to database
        await trainer.save(session)
        print(f"Created trainer profile with UUID: {trainer.uuid}")
        
        # Create availability for the trainer
        now = datetime.now()
        availability = Availability(
            trainer_id=trainer_user.uuid,
            start_time=now + timedelta(days=1, hours=9),
            end_time=now + timedelta(days=1, hours=10),
            is_available=True
        )
        
        # Save availability to database
        await availability.save(session)
        print(f"Created availability with UUID: {availability.uuid}")
        
        # Create an appointment
        appointment = Appointment(
            trainer_id=trainer_user.uuid,
            client_id=client_user.uuid,
            appointment_time=now + timedelta(days=1, hours=9, minutes=30),
            status=AppointmentStatus.SCHEDULED
        )
        
        # Save appointment to database
        await appointment.save(session)
        print(f"Created appointment with UUID: {appointment.uuid}")
        
        # Create feedback for the appointment
        feedback = Feedback(
            appointment_id=appointment.uuid,
            rating=5,
            comments="Great session! Very knowledgeable trainer."
        )
        
        # Save feedback to database
        await feedback.save(session)
        print(f"Created feedback with UUID: {feedback.uuid}")
        
        # Retrieve and verify data
        print("\nRetrieving data from database...")
        
        # Get users
        users = await session.execute("SELECT * FROM \"user\"")
        users = users.fetchall()
        print(f"Number of users: {len(users)}")
        
        # Get trainers
        trainers = await session.execute("SELECT * FROM trainer")
        trainers = trainers.fetchall()
        print(f"Number of trainers: {len(trainers)}")
        
        # Get appointments
        appointments = await session.execute("SELECT * FROM appointment")
        appointments = appointments.fetchall()
        print(f"Number of appointments: {len(appointments)}")
        
        # Get feedback
        feedbacks = await session.execute("SELECT * FROM feedback")
        feedbacks = feedbacks.fetchall()
        print(f"Number of feedback entries: {len(feedbacks)}")
        
        # Get availability
        availabilities = await session.execute("SELECT * FROM availability")
        availabilities = availabilities.fetchall()
        print(f"Number of availability entries: {len(availabilities)}")
        
        print("\nDatabase test completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_database()) 