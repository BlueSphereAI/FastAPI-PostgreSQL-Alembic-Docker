from typing import Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.report.model import Report


class ReportService(BaseService):
    """
    Report service for report management
    """

    async def create_report(self, compound_id: UUID, content: bytes) -> Report:
        """
        Create a new report
        """
        report = Report(compound_id=compound_id, content=content)
        await report.save(self.db_session)
        return report

    async def get_report_by_id(self, report_id: UUID) -> Optional[Report]:
        """
        Get report by ID
        """
        query = select(Report).where(Report.uuid == report_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_report_by_compound(self, compound_id: UUID) -> Optional[Report]:
        """
        Get report by compound ID
        """
        query = select(Report).where(Report.compound_id == compound_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none() 