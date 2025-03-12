from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.repurposing_suggestion.model import RepurposingSuggestion


class RepurposingSuggestionService(BaseService):
    """
    Repurposing Suggestion service for repurposing suggestion management
    """

    async def create_repurposing_suggestion(
        self, compound_id: UUID, therapeutic_area: str, suggestion_details: str
    ) -> RepurposingSuggestion:
        """
        Create a new repurposing suggestion
        """
        suggestion = RepurposingSuggestion(
            compound_id=compound_id,
            therapeutic_area=therapeutic_area,
            suggestion_details=suggestion_details
        )
        await suggestion.save(self.db_session)
        return suggestion

    async def get_repurposing_suggestion_by_id(self, suggestion_id: UUID) -> Optional[RepurposingSuggestion]:
        """
        Get repurposing suggestion by ID
        """
        query = select(RepurposingSuggestion).where(RepurposingSuggestion.uuid == suggestion_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_repurposing_suggestions_by_compound(self, compound_id: UUID) -> List[RepurposingSuggestion]:
        """
        Get all repurposing suggestions for a compound
        """
        query = select(RepurposingSuggestion).where(RepurposingSuggestion.compound_id == compound_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()
        
    async def create_mock_suggestions(self, compound_id: UUID) -> List[RepurposingSuggestion]:
        """
        Create mock repurposing suggestions for a compound
        """
        # Sample therapeutic areas and suggestions
        suggestions_data = [
            {
                "therapeutic_area": "Neurodegenerative Disorders",
                "suggestion_details": "The compound shows potential for targeting beta-amyloid aggregation, which could be beneficial for Alzheimer's disease treatment."
            },
            {
                "therapeutic_area": "Inflammatory Conditions",
                "suggestion_details": "The molecular structure suggests anti-inflammatory properties that could be effective for rheumatoid arthritis or inflammatory bowel disease."
            },
            {
                "therapeutic_area": "Metabolic Disorders",
                "suggestion_details": "The binding profile indicates potential interaction with glucose metabolism pathways, suggesting applications in type 2 diabetes."
            }
        ]
        
        created_suggestions = []
        for data in suggestions_data:
            suggestion = await self.create_repurposing_suggestion(
                compound_id=compound_id,
                therapeutic_area=data["therapeutic_area"],
                suggestion_details=data["suggestion_details"]
            )
            created_suggestions.append(suggestion)
            
        return created_suggestions 