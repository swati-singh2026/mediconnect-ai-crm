import { createSlice } from "@reduxjs/toolkit";

interface InteractionState {
  interactions: any[];
}

const initialState: InteractionState = {
  interactions: [],
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    addInteraction: (state, action) => {
      state.interactions.push(action.payload);
    },

    updateInteraction: (state, action) => {
      const index = state.interactions.findIndex(
        (item: any) => item.id === action.payload.id,
      );

      if (index !== -1) {
        state.interactions[index] = action.payload;
      }
    },
  },
});

export const { addInteraction, updateInteraction } = interactionSlice.actions;

export default interactionSlice.reducer;
