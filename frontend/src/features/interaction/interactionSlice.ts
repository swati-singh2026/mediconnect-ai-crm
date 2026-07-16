import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface Interaction {
  id?: number;
  [key: string]: any;
}

interface InteractionState {
  interactions: Interaction[];
  loading: boolean;
  currentChat: string;
  error: string | null;
}

const initialState: InteractionState = {
  interactions: [],
  loading: false,
  currentChat: "",
  error: null,
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    addInteraction: (state, action: PayloadAction<Interaction>) => {
      state.interactions.push(action.payload);
    },

    updateInteraction: (state, action: PayloadAction<Interaction>) => {
      const index = state.interactions.findIndex(
        (item) => item.id === action.payload.id,
      );

      if (index !== -1) {
        state.interactions[index] = action.payload;
      }
    },

    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    },

    setCurrentChat: (state, action: PayloadAction<string>) => {
      state.currentChat = action.payload;
    },

    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload;
    },
  },
});

export const {
  addInteraction,
  updateInteraction,
  setLoading,
  setCurrentChat,
  setError,
} = interactionSlice.actions;

export default interactionSlice.reducer;
